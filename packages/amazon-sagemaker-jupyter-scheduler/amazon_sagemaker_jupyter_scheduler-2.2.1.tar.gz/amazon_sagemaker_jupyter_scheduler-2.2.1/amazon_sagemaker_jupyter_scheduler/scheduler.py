import os
import asyncio
import json
from aws_embedded_metrics.logger.metrics_context import MetricsContext

import botocore
from typing import List, Dict, Type, Optional, Union

from jupyter_scheduler.environments import EnvironmentManager
from jupyter_scheduler.models import (
    DescribeJob,
    ListJobDefinitionsQuery,
    DescribeJobDefinition,
    UpdateJob,
    ListJobsQuery,
    ListJobsResponse,
    CountJobsQuery,
    CreateJobDefinition,
    CreateJob,
    ListJobDefinitionsResponse,
    UpdateJobDefinition,
    CreateJobFromDefinition,
    Status,
)
from jupyter_scheduler.scheduler import BaseScheduler
from jupyter_scheduler.exceptions import SchedulerError
from amazon_sagemaker_jupyter_scheduler.aws_config import get_aws_account_id
from amazon_sagemaker_jupyter_scheduler.internal_metadata_adapter import (
    InternalMetadataAdapter,
)

from amazon_sagemaker_jupyter_scheduler.logging import async_with_metrics

from amazon_sagemaker_jupyter_scheduler.app_metadata import (
    get_partition,
    get_region_name,
)

from amazon_sagemaker_jupyter_scheduler.clients import (
    get_sagemaker_client,
    SageMakerAsyncBoto3Client,
    EventBridgeAsyncBotoClient,
    S3AsyncBoto3Client,
    get_s3_client,
    get_event_bridge_client,
)
from amazon_sagemaker_jupyter_scheduler.cron_util import (
    EventBridgeCronExpressionAdapter,
    DEFAULT_CRON_EXPRESSION,
)
from amazon_sagemaker_jupyter_scheduler.deletable_resource import (
    DeletableResourceContainer,
    DeletableResource,
)
from amazon_sagemaker_jupyter_scheduler.providers.tags import get_resource_create_tags
from amazon_sagemaker_jupyter_scheduler.s3_uri import S3URI
from amazon_sagemaker_jupyter_scheduler.utils import (
    generate_job_identifier,
    get_pipeline_expression_output_name,
    sanitize_string,
)
from amazon_sagemaker_jupyter_scheduler.error_util import (
    SageMakerSchedulerError,
    ErrorMatcher,
    ErrorConverter,
    ErrorFactory,
)
from amazon_sagemaker_jupyter_scheduler.file_uploader import S3FileUploader
from amazon_sagemaker_jupyter_scheduler.models import (
    JobTag,
    EventBridgeRuleStatus,
    JobEnvironmentVariableName,
    RuntimeEnvironmentParameterName,
)
from amazon_sagemaker_jupyter_scheduler.model_converter import ModelConverter
from amazon_sagemaker_jupyter_scheduler.runtime_environment_parameters import (
    RuntimeEnvironmentParameters,
)

EVENT_BRIDGE_RULE_TARGET_ID = "notebook-execution"
SAGEMAKER_PIPELINE_STEP_NAME = "notebook-execution"


class SageMakerScheduler(BaseScheduler):
    """
    This is the template class that will execute logic based on the environment it is being executed in
    """

    task_runner = None

    def __init__(
        self,
        root_dir: str,
        environments_manager: Type[EnvironmentManager],
        config=None,
        sagemaker_client: SageMakerAsyncBoto3Client = None,
        event_bridge_client: EventBridgeAsyncBotoClient = None,
        s3_client: S3AsyncBoto3Client = None,
        converter: ModelConverter = None,
        error_matcher: ErrorMatcher = None,
        error_converter: ErrorConverter = None,
        error_factory: ErrorFactory = None,
        **kwargs,
    ):
        super().__init__(
            root_dir=root_dir,
            environments_manager=environments_manager,
            config=config,
            **kwargs,
        )
        self.root_dir = root_dir
        self.config = config
        self.current_environment = environments_manager.current_environment
        self._sagemaker_client = sagemaker_client or get_sagemaker_client()
        self._event_bridge_client = event_bridge_client or get_event_bridge_client()
        self._s3_client = s3_client or get_s3_client()
        self.converter = converter or ModelConverter(self.log)
        self.error_matcher = error_matcher or ErrorMatcher()
        self.error_converter = error_converter or ErrorConverter()
        self.error_factory = error_factory or ErrorFactory()

    def sagemaker_client(self):
        return self._sagemaker_client

    def s3_client(self):
        return self._s3_client

    def event_bridge_client(self):
        return self._event_bridge_client

    async def get_additional_tags(self) -> List[Dict]:
        return []

    async def _get_system_dependencies_version(
        self, stage_name: str, region_name: str
    ) -> str:
        # TODO: new region addition should have a way to read from a config if we get into bucket snpping
        # TODO: handle errors like network, permission issues
        s3_bucket_name = f"sagemakerheadlessexecution-{stage_name}-{region_name}"

        try:
            response_content = await self.s3_client().get_object_content(
                bucket=s3_bucket_name, key="headless_system_dependencies/latest"
            )
        except botocore.exceptions.ClientError as error:
            raise SageMakerSchedulerError.from_boto_error(
                error,
                f"Retrieving Notebook Execution driver from service s3 bucket - {s3_bucket_name} failed",
            )
        self.log.info("Successfully called S3 GetObject for system dependencies")
        latest_file = json.loads(response_content)
        self.log.info(f"S3 response for {s3_bucket_name} with {latest_file}")
        return f"s3://{s3_bucket_name}/headless_system_dependencies/build_{latest_file['latest']}"

    def handle_aws_client_error(self, error, log_message=None):
        if isinstance(error, SchedulerError):
            raise error
        elif isinstance(error, botocore.exceptions.ClientError):
            if log_message is not None:
                self.log.error(f"Boto client Error: {log_message}")
            raise SageMakerSchedulerError.from_boto_error(error)
        elif isinstance(error, RuntimeError):
            if log_message is not None:
                self.log.error(f"Runtime Error: {log_message}")
            raise SageMakerSchedulerError.from_runtime_error(error)
        elif isinstance(error, FileNotFoundError):
            self.log.error(f"File not found error: {str(error)}")
            raise SchedulerError(str(error))
        elif isinstance(error, botocore.exceptions.NoCredentialsError):
            self.log.error(f"No Credentials Error: {log_message}")
            raise SageMakerSchedulerError.from_no_credentials_error(error)
        else:
            if log_message is None:
                raise error
            else:
                self.log.error(log_message)
                raise self.error_factory.internal_error(error) from error

    async def _verify_bucket_region_and_owner(self, bucket_name: str):
        bucket_location = await self.s3_client().get_bucket_location(
            bucket=bucket_name, accountId=await get_aws_account_id()
        )

        # LocationConstraint will be null when bucket is in us-east-1
        bucket_region = bucket_location["LocationConstraint"] or "us-east-1"
        if bucket_region != get_region_name():
            raise SchedulerError(
                f"S3 bucket {bucket_name} must be in region '{get_region_name()}', but found in '{bucket_region}'"
            )

    async def _prepare_job_artifacts(
        self,
        deletable_resources: DeletableResourceContainer,
        training_job_name: str,
        s3_uri: str,
        runtime_environment_parameters: RuntimeEnvironmentParameters,
        root_dir: str,
    ) -> S3FileUploader:
        input_uri = S3URI(runtime_environment_parameters.s3_input)
        output_uri = S3URI(runtime_environment_parameters.s3_output)

        try:
            if input_uri.bucket == output_uri.bucket:
                await self._verify_bucket_region_and_owner(input_uri.bucket)
            else:
                await asyncio.gather(
                    self._verify_bucket_region_and_owner(input_uri.bucket),
                    self._verify_bucket_region_and_owner(output_uri.bucket),
                )
        except botocore.exceptions.ClientError as error:
            raise SageMakerSchedulerError.from_boto_error(
                error,
                f"GetBucketLocation failed for {set([input_uri.bucket, output_uri.bucket])}",
            )

        s3_file_uploader = S3FileUploader(
            deletable_resources,
            runtime_environment_parameters.s3_input,
            training_job_name,
            s3_uri,
            runtime_environment_parameters.sm_init_script,
            runtime_environment_parameters.sm_lcc_init_script_arn,
            root_dir,
        )

        self.log.info(f"Uploading artifacts for job {training_job_name}...")
        try:
            await s3_file_uploader.upload()
        except Exception as error:
            raise SageMakerSchedulerError.from_boto_error(
                error, f"Uploading artifacts to S3 bucket failed - {input_uri.bucket}"
            )

        self.log.info(f"Successfully uploaded artifacts for job {training_job_name}.")

        return s3_file_uploader

    @async_with_metrics("CreateJob")
    async def create_job(self, input: CreateJob, metrics: MetricsContext) -> str:
        """
        The SageMaker implementation of `POST scheduler/jobs`

        # TODO: better documentation
        """

        # log the input parameters
        self.log.info(f"Input parameters for create_job: {input}")

        training_job_name = generate_job_identifier(
            name=input.name,
            notebook_name=os.path.splitext(os.path.basename(input.input_uri))[0],
        )
        metrics.set_property("Id", training_job_name)

        deletable_resources = DeletableResourceContainer(self.log)

        try:
            s3_file_uploader = await self._prepare_job_artifacts(
                deletable_resources=deletable_resources,
                training_job_name=training_job_name,
                s3_uri=input.input_uri,
                runtime_environment_parameters=RuntimeEnvironmentParameters(
                    input.runtime_environment_parameters
                ),
                root_dir=self.root_dir,
            )

            self.log.info(f"Getting S3 dependency Uri...")
            stage = InternalMetadataAdapter().get_stage()
            s3_dependency_uri = await self._get_system_dependencies_version(
                stage, get_region_name()
            )
            self.log.info(f"Successfully got S3 dependency Uri")

            create_training_job_input = (
                await self.converter.to_create_training_job_input(
                    training_job_name=training_job_name,
                    upstream_model=input,
                    s3_file_uploader=s3_file_uploader,
                    s3_dependency_uri=s3_dependency_uri,
                )
            )

            create_training_job_input["TrainingJobName"] = training_job_name

            self.log.info(
                f"Calling SageMaker CreateTrainingJob for job {training_job_name}..."
            )

            try:
                create_training_job_input["Tags"] = await get_resource_create_tags(
                    job_name=input.name,
                    notebook_name=s3_file_uploader.notebook_name,
                    headless_driver_version="false",  # TODO: Update this to the correct version
                    logger=self.log,
                )

                # log the create_training_job_input
                self.log.info(f"create_training_job_input: {create_training_job_input}")

                await self.sagemaker_client().create_training_job(
                    create_training_job_input
                )
            except Exception as error:
                self.log.error(
                    f"Error when calling SageMaker CreateTrainingJob or ListTags with job {training_job_name}: {error}"
                )
                raise error

            # All operations succeeded, so don't delete any resources.
            deletable_resources.clear()

        except Exception as error:
            self.handle_aws_client_error(error)
        finally:
            await deletable_resources.delete_all()

        self.log.info(
            f"Successfully called SageMaker CreateTrainingJob for job {training_job_name}."
        )

        return training_job_name

    @async_with_metrics("CreateJobFromJobDefinition")
    async def create_job_from_definition(
        self,
        job_definition_id: str,
        model: CreateJobFromDefinition,
        metrics: MetricsContext,
    ):
        try:
            metrics.set_property("Id", job_definition_id)
            self.log.info(
                f"Calling SageMaker DescribePipeline for pipeline {job_definition_id}..."
            )
            describe_pipeline_response = (
                await self.sagemaker_client().describe_pipeline(job_definition_id)
            )
            self.log.info(
                f"Successfully called SageMaker DescribePipeline for pipeline {job_definition_id}."
            )

            training_job_details = json.loads(
                describe_pipeline_response["PipelineDefinition"]
            )["Steps"][0]["Arguments"]

            environment = training_job_details["Environment"]

            tag_dict = self.converter.to_tag_dict(training_job_details["Tags"])
            job_name = tag_dict[JobTag.NOTEBOOK_NAME.value]
            notebook_name = environment[
                JobEnvironmentVariableName.SM_INPUT_NOTEBOOK_NAME.value
            ]

            # Overwrite output notebook name, since the Pipeline definition currently has a parameterized name.
            environment[
                JobEnvironmentVariableName.SM_OUTPUT_NOTEBOOK_NAME.value
            ] = self.converter.generate_training_job_name(
                job_name=job_name,
                notebook_name=notebook_name,
            )

            job_id = generate_job_identifier(
                name=job_name,
                notebook_name=os.path.splitext(notebook_name)[0],
            )

            training_job_details["TrainingJobName"] = job_id
            training_job_details["HyperParameters"] = model.parameters or {}

            self.log.info(f"Calling SageMaker CreateTrainingJob for job {job_id}...")
            await self.sagemaker_client().create_training_job(training_job_details)
            self.log.info(
                f"Successfully called SageMaker CreateTrainingJob for job {job_id}."
            )
            return job_id
        except Exception as error:
            raise self.handle_aws_client_error(error)

    async def update_job(self, job_id: str, model: UpdateJob):
        """Updates job metadata in the persistence store,
        for example name, status etc. In case of status
        change to STOPPED, should call stop_job
        """
        pass

    @async_with_metrics("ListJobs")
    async def list_jobs(
        self, query: ListJobsQuery, metrics: MetricsContext
    ) -> ListJobsResponse:
        """Returns list of all jobs filtered by query"""

        self.log.info("Calling SageMaker Search...")

        try:
            training_job_list_response = await self.sagemaker_client().search(
                self.converter.to_training_job_search_input(query)
            )
        except Exception as error:
            self.handle_aws_client_error(
                error, f"Error when calling SageMaker Search: {error}"
            )

        self.log.info("Successfully called SageMaker Search.")

        return self.converter.to_jupyter_list_jobs_response(
            self, training_job_list_response
        )

    async def count_jobs(self, query: CountJobsQuery) -> int:
        """Returns number of jobs filtered by query"""
        pass

    @async_with_metrics("DescribeJob")
    async def get_job(
        self,
        job_id: str,
        outputs: Optional[bool] = True,
        metrics: MetricsContext = None,
    ) -> DescribeJob:
        """Returns job record for a single job"""

        self.log.info(f"Calling SageMaker DescribeTrainingJob for job {job_id}...")

        try:
            training_job_response = await self.sagemaker_client().describe_training_job(
                job_name=job_id
            )
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling SageMaker DescribeTrainingJob for job {job_id}: {error}",
            )

        self.log.info(
            f"Successfully called SageMaker DescribeTrainingJob for job {job_id}."
        )

        # Extract the Training Job ARN from the response since its case might differ from the Training Job Name.
        resource_arn = training_job_response["TrainingJobArn"]

        self.log.info(f"Calling SageMaker ListTags for {resource_arn}...")

        try:
            list_tags_response = await self.sagemaker_client().list_tags(
                resource_arn=resource_arn
            )
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling SageMaker ListTags for {resource_arn}: {error}",
            )

        self.log.info(f"Successfully called SageMaker ListTags for {resource_arn}.")

        return self.converter.to_jupyter_describe_job_output(
            scheduler=self,
            outputs=outputs,
            training_job_response=training_job_response,
            tag_dict=self.converter.to_tag_dict(list_tags_response["Tags"]),
        )

    @async_with_metrics("DeleteJob")
    async def delete_job(self, job_id: str, metrics: MetricsContext):
        """Deletes the job record, stops the job if running"""

        metrics.set_property("Id", job_id)

        # Call DescribeTrainingJob to get the ARN, since its case does not necessarily not match the training job name.
        self.log.info(f"Calling SageMaker DescribeTrainingJob for job {job_id}...")
        training_job_details = await self.sagemaker_client().describe_training_job(
            job_id
        )
        self.log.info(
            f"Successfully called SageMaker DescribeTrainingJob for job {job_id}..."
        )

        resource_arn = training_job_details["TrainingJobArn"]

        self.log.info(f"Calling SageMaker StopTrainingJob for job {job_id}...")
        self.log.info(f"Calling SageMaker ListTags for {resource_arn}...")

        [stop_job_response, add_tag_response] = await asyncio.gather(
            self.sagemaker_client().stop_training_job(training_job_name=job_id),
            self.sagemaker_client().add_tags(
                resource_arn=resource_arn,
                tag_list=self.converter.to_tag_list(
                    {JobTag.IS_STUDIO_ARCHIVED.value: "true"}
                ),
            ),
            return_exceptions=True,
        )

        if isinstance(stop_job_response, botocore.exceptions.ClientError):
            if not self.error_matcher.is_training_job_status_validation_error(
                stop_job_response
            ):
                self.log.error(
                    f"Boto client error when calling SageMaker StopTrainingJob for job {job_id}: {stop_job_response}"
                )
                raise self.error_converter.boto_error_to_web_error(
                    stop_job_response
                ) from stop_job_response
        elif isinstance(stop_job_response, Exception):
            self.log.error(
                f"Error when calling SageMaker StopTrainingJob for job {job_id}: {stop_job_response}"
            )
            raise self.error_factory.internal_error(
                stop_job_response
            ) from stop_job_response

        self.log.info(
            f"Successfully called SageMaker StopTrainingJob for job {job_id}."
        )

        if isinstance(add_tag_response, Exception):
            self.log.error(
                f"Error when calling SageMaker AddTags for {resource_arn}: {add_tag_response}"
            )
            raise self.error_factory.internal_error(
                add_tag_response
            ) from add_tag_response

        self.log.info(f"Successfully called SageMaker ListTags for {resource_arn}.")

    @async_with_metrics("StopJob")
    async def stop_job(self, job_id: str, metrics: MetricsContext):
        """Stops the job, this is not analogous
        to the REST API that will be called to
        stop the job. Front end will call the PUT
        API with status update to STOPPED, which will
        call the update_job method. This method is
        supposed to do the work of actually stopping
        the process that is executing the job. In case
        of a task runner, you can assume a call to task
        runner to suspend the job.
        """

        metrics.set_property("Id", job_id)
        self.log.info(f"Calling SageMaker StopTrainingJob for job {job_id}...")

        try:
            await self.sagemaker_client().stop_training_job(job_id)
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling SageMaker StopTrainingJob for job {job_id}: {error}",
            )

        self.log.info(
            f"Successfully called SageMaker StopTrainingJob for job {job_id}."
        )

    def get_created_resources_description_text(self):
        return "Created for Notebook execution from notebook scheduler"

    @async_with_metrics("CreateJobDefinition")
    async def create_job_definition(
        self, model: CreateJobDefinition, metrics: MetricsContext
    ) -> str:
        """Creates a new job definition record,
        consider this as the template for creating
        recurring/scheduled jobs.
        """
        cron_expression = EventBridgeCronExpressionAdapter(
            model.schedule if model.schedule else DEFAULT_CRON_EXPRESSION
        ).cron_expression

        schedule_expression = f"cron({cron_expression})"

        # 1. S3 -- Prepare the training job artifacts.
        job_definition_id = generate_job_identifier(
            name=model.name,
            notebook_name=os.path.splitext(os.path.basename(model.input_uri))[0],
        )

        metrics.set_property("Id", job_definition_id)

        runtime_environment_parameters = RuntimeEnvironmentParameters(
            model.runtime_environment_parameters
        )

        deletable_resources = DeletableResourceContainer(self.log)

        try:
            s3_file_uploader = await self._prepare_job_artifacts(
                deletable_resources=deletable_resources,
                training_job_name=job_definition_id,
                s3_uri=model.input_uri,
                runtime_environment_parameters=runtime_environment_parameters,
                root_dir=self.root_dir,
            )

            # 2. SageMaker:CreatePipeline
            self.log.info(
                f"Calling SageMaker CreatePipeline for job definition {job_definition_id}"
            )

            stage = InternalMetadataAdapter().get_stage()
            s3_dependency_uri = await self._get_system_dependencies_version(
                stage, get_region_name()
            )
            create_training_job_input = (
                await self.converter.to_create_training_job_input(
                    training_job_name=job_definition_id,
                    upstream_model=model,
                    s3_file_uploader=s3_file_uploader,
                    s3_dependency_uri=s3_dependency_uri,
                )
            )
            create_training_job_input["RetryStrategy"]["MaximumRetryAttempts"] = 1

            common_tags = []

            try:
                common_tags = await get_resource_create_tags(
                    job_name=model.name,
                    notebook_name=s3_file_uploader.notebook_name,
                    headless_driver_version="false",  # TODO: Update this to the correct version
                    logger=self.log,
                )

                # adding to an empty list to avoid overriding pipeline tags
                create_training_job_input["Tags"] = [] + common_tags

                # log the create_training_job_input
                self.log.info(f"create_training_job_input: {create_training_job_input}")

                create_training_job_input["Tags"].append(
                    {
                        "Key": "sagemaker:job-definition-id",
                        "Value": job_definition_id,
                    }
                )
                # this expression will be evaluated every time the pipeline gets executed
                # and each output will have the timestamp as suffix
                [notebook_name_without_ext, notebook_extension] = os.path.splitext(
                    s3_file_uploader.notebook_name
                )
                create_training_job_input["Environment"][
                    JobEnvironmentVariableName.SM_OUTPUT_NOTEBOOK_NAME.value
                ] = get_pipeline_expression_output_name(
                    model.name, notebook_name_without_ext, notebook_extension
                )
                maxAttempts = runtime_environment_parameters.max_retry_attempts if hasattr(runtime_environment_parameters, "max_retry_attempts") else 1
                maxAttempts = int(maxAttempts)
                pipeline_result = await self.sagemaker_client().create_pipeline(
                    pipeline_name=job_definition_id,
                    pipeline_display_name=sanitize_string(model.name, 63),
                    pipeline_description=self.get_created_resources_description_text(),
                    pipeline_definition=json.dumps(
                        {
                            "Version": "2020-12-01",
                            "Parameters": [],
                            "Steps": [
                                {
                                    "Name": f"{sanitize_string(model.name, 10)}-{sanitize_string(notebook_name_without_ext, 10)}",
                                    "Type": "Training",
                                    "Arguments": create_training_job_input,
                                    "RetryPolicies": [
                                        {
                                            "ExceptionType": [
                                                "Step.SERVICE_FAULT",
                                                "Step.THROTTLING",
                                                "SageMaker.JOB_INTERNAL_ERROR",
                                                "SageMaker.CAPACITY_ERROR",
                                                "SageMaker.RESOURCE_LIMIT"
                                            ],
                                            "MaxAttempts": maxAttempts,
                                        },
                                    ],
                                }
                            ],
                        }
                    ),
                    role_arn=runtime_environment_parameters.role_arn,
                    tags=common_tags,
                )
            except Exception as error:
                self.log.error(
                    f"Error when calling SageMaker CreatePipeline for job definition {job_definition_id}: {error}"
                )
                raise error

            pipeline_arn = pipeline_result["PipelineArn"]
            deletable_resources.add_resource(
                DeletableResource(
                    pipeline_arn,
                    lambda: self.sagemaker_client().delete_pipeline(job_definition_id),
                )
            )

            self.log.info(
                f"Successfully called SageMaker CreatePipeline: {pipeline_arn}."
            )

            # 3. EventBridge:PutRule
            self.log.info(f"Calling EventBridge PutRule for pipeline {pipeline_arn}...")

            try:
                put_rule_result = await self.event_bridge_client().put_rule(
                    name=job_definition_id,
                    description=self.get_created_resources_description_text(),
                    schedule_expression=schedule_expression,
                    state=EventBridgeRuleStatus.ENABLED.value,
                    tags=common_tags,
                )
            except Exception as error:
                self.log.error(
                    f"Error when calling EventBridge PutRule for job definition {job_definition_id}: {error}"
                )
                raise error

            rule_arn = put_rule_result["RuleArn"]
            deletable_resources.add_resource(
                DeletableResource(
                    rule_arn,
                    lambda: self.event_bridge_client().delete_rule(job_definition_id),
                )
            )

            self.log.info(f"Successfully called EventBridge PutRule: {rule_arn}")

            # 4. EventBridge:PutTargets
            self.log.info(f"Calling EventBridge PutTargets for rule {rule_arn}...")

            try:
                await self.event_bridge_client().put_targets(
                    rule_name=job_definition_id,
                    targets=[
                        {
                            "Id": EVENT_BRIDGE_RULE_TARGET_ID,
                            "Arn": pipeline_arn,
                            "RoleArn": runtime_environment_parameters.role_arn,
                        }
                    ],
                )
            except Exception as error:
                self.log.error(
                    f"Error when calling EventBridge PutTargets for rule {rule_arn}: {error}"
                )
                raise error

            # All operations succeeded, so don't delete any resources.
            deletable_resources.clear()

        except Exception as error:
            self.handle_aws_client_error(error)
        finally:
            await deletable_resources.delete_all()

        self.log.info(f"Successfully called EventBridge PutTargets for rule {rule_arn}")

        return job_definition_id

    async def _update_job_definition(
        self, job_definition_id: str, model: UpdateJobDefinition
    ):
        cron_expression = EventBridgeCronExpressionAdapter(model.schedule).cron_expression
        schedule_expression = f"cron({cron_expression})"

        self.log.info(f"Calling EventBridge PutRule for rule {job_definition_id}...")

        try:
            await self.event_bridge_client().put_rule(
                name=job_definition_id,
                description=self.get_created_resources_description_text(),
                schedule_expression=schedule_expression,
                state=EventBridgeRuleStatus.ENABLED.value,
            )
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling EventBridge PutRule for rule {job_definition_id}: {error}",
            )

        self.log.info(
            f"Successfully called EventBridge PutRule for rule {job_definition_id}"
        )

    @async_with_metrics("UpdateJobDefinition")
    async def update_job_definition(
        self,
        job_definition_id: str,
        model: UpdateJobDefinition,
        metrics: MetricsContext,
    ):
        """Updates job definition metadata in the persistence store,
        should only impact all future jobs.
        """
        metrics.set_property("Id", job_definition_id)
        enable = disable = update = 0

        try:
            if model.active is None:
                update = 1
                await self._update_job_definition(job_definition_id, model)
            elif model.active:
                enable = 1
                await self.event_bridge_client().enable_rule(job_definition_id)
            else:
                disable = 1
                await self.event_bridge_client().disable_rule(job_definition_id)
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling EventBridge PutRule for rule {job_definition_id}: {error}",
            )

        metrics.put_metric("Enable", enable)
        metrics.put_metric("Disable", disable)
        metrics.put_metric("Update", update)

    @async_with_metrics("DeleteJobDefinition")
    async def delete_job_definition(
        self, job_definition_id: str, metrics: MetricsContext
    ):
        """Deletes the job definition record,
        implementors can optionally stop all running jobs
        """
        try:
            metrics.set_property("Id", job_definition_id)

            # Pause the job definition first, to avoid creating jobs while trying to delete the pipeline.
            # This is safe to call while the rule is already disabled.
            await self.event_bridge_client().disable_rule(job_definition_id)

            # Try to delete the pipeline before anything else.
            # This will raise an error if there are pending executions.
            await self.sagemaker_client().delete_pipeline(job_definition_id)

            # Once the pipeline has been successfully deleted, proceed to delete the Event Bridge rule.
            # The Event Bridge Rule cannot be deleted until all targets have been removed.
            await self.event_bridge_client().remove_targets(
                # ID name is hardcoded during create job definition time
                job_definition_id,
                [EVENT_BRIDGE_RULE_TARGET_ID],
            )

            # This will fail if the customer independently added other targets (which we don't expect them to do).
            await self.event_bridge_client().delete_rule(job_definition_id)
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling - delete_job_definition - {job_definition_id}: {error}",
            )

    @async_with_metrics("GetJobDefinition")
    async def get_job_definition(
        self,
        job_definition_id: str,
        list_tags_response: Dict = None,
        metrics: MetricsContext = None,
    ) -> DescribeJobDefinition:
        """Returns job definition record for a single job definition"""
        self.log.info(f"Calling Sagemaker Describe Pipeline for {job_definition_id}...")
        # We will invoke one api call to get all associated tags for a given job_definition,
        # as tags will be stored in both SM Pipeline and Eventbridge rule
        try:
            metrics.set_property("Id", job_definition_id)
            [describe_pipeline, describe_event_rule] = await asyncio.gather(
                self.sagemaker_client().describe_pipeline(job_definition_id),
                self.event_bridge_client().describe_rule(job_definition_id),
            )
        except Exception as error:
            self.handle_aws_client_error(
                error,
                f"Error when calling - get_job_definition - {job_definition_id}: {error}",
            )

        self.log.info(
            f"Successfully called SageMaker Describe Pipeline for {job_definition_id}."
        )

        if not list_tags_response:
            self.log.info(
                f"Calling SageMaker ListTags for pipeline {job_definition_id}..."
            )
            list_tags_response = await self.sagemaker_client().list_tags(
                resource_arn=describe_pipeline["PipelineArn"]
            )
            self.log.info(
                f"Successfully called SageMaker ListTags for pipeline {job_definition_id}."
            )

        return self.converter.to_jupyter_describe_job_definition_output(
            job_definition_id=job_definition_id,
            describe_pipeline_response=describe_pipeline,
            describe_event_rule_response=describe_event_rule,
            list_tags_response=list_tags_response,
        )

    @async_with_metrics("ListJobDefinition")
    async def list_job_definitions(
        self, query: ListJobDefinitionsQuery, metrics: MetricsContext
    ) -> ListJobDefinitionsResponse:
        """Returns list of all job definitions filtered by query"""

        self.log.info("Calling SageMaker Search...")

        try:
            pipeline_list_response = await self.sagemaker_client().search(
                self.converter.to_pipeline_seach_input(query)
            )
        except Exception as error:
            self.handle_aws_client_error(
                error,
                self.log.error(f"Error when calling list_job_definitions : {error}"),
            )

        pipeline_results = pipeline_list_response["Results"]

        # Get details for each JobDefinition in parallel. Query max results on the UI is currently 25.
        # SageMaker:DescribePipeline default burst rate is 100 TPS
        # Events:DescribeRule default rate is 50 TPS
        # https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-quota.html
        job_definition_results = await asyncio.gather(
            *[
                self.get_job_definition(
                    item["Pipeline"]["PipelineName"],
                    # Optimization: Skip the ListTags in get_job_definition since tags are in Search results
                    list_tags_response=({"Tags": item["Pipeline"]["Tags"]}),
                )
                for item in pipeline_results
            ],
            return_exceptions=True,
        )

        successful_job_definitions: List[DescribeJobDefinition] = []

        for idx, describe_job_definition in enumerate(job_definition_results):
            # TODO: Better error handling. This is just so half-created job definitions don't break the UI.
            if isinstance(describe_job_definition, DescribeJobDefinition):
                successful_job_definitions.append(describe_job_definition)
            else:
                pipeline = pipeline_results[idx]["Pipeline"]
                self.log.error(
                    f"Error when getting job definition for {pipeline['PipelineArn']} : {describe_job_definition}"
                )

        return ListJobDefinitionsResponse(
            job_definitions=successful_job_definitions,
            next_token=pipeline_list_response.get("NextToken", None),
            total_count=-1,
        )

    async def get_staging_paths(
        self, model: Union[DescribeJob, DescribeJobDefinition]
    ) -> Dict[str, str]:
        """Returns full staging paths for all job files

        Notes
        -----
        Any path supported by `fsspec https://filesystem-spec.readthedocs.io/en/latest/index.html`_
        is a valid return value. For staging files that
        are stored as tar or compressed tar archives, this
        should specify the first entry with a key as `tar`
        or `tar.gz` and value as path to the archive file;
        the values for the actual format files will be just
        the path to them in the archive, in most cases just
        the filename. For input files, the key 'input' is
        expected.


        Examples
        --------
        >>> self.get_staging_paths(1)
        {
            'ipynb': '/job_files/helloworld-2022-10-10.ipynb',
            'html': '/job_files/helloworld-2022-10-10.html',
            'input': '/job_files/helloworld.ipynb'
        }

        For files that are archived as tar or compressed tar
        >>> self.get_staging_paths(2)
        {
            'tar.gz': '/job_files/helloworld.tar.gz',
            'ipynb': 'helloworld-2022-10-10.ipynb',
            'html': 'helloworld-2022-10-10.html',
            'input': 'helloworld.ipynb'
        }

        Parameters
        ----------
        job_id : str
            Unique identifier for the job

        Returns
        -------
        Dictionary with keys as output format and values
        as full path to the job file in staging location.
        """
        if not isinstance(model, DescribeJob):
            raise NotImplementedError("Cannot get staging paths for a job definition")

        training_job_response = await self.sagemaker_client().describe_training_job(
            job_name=model.job_id
        )

        original_output_file_name = (
            training_job_response.get("Environment", {})
            .get(JobEnvironmentVariableName.SM_OUTPUT_NOTEBOOK_NAME.value)
            .replace("Z-.ipynb", "Z.ipynb")
            .replace(":", "-")
        )

        # From: hello-7-Hello-2022-10-24T18:59:43.851Z-.ipynb
        #   To: hello-7-Hello-2022-10-24T18-59-43-851Z.ipynb
        output_filename_parts = os.path.splitext(original_output_file_name)

        # Define all known output formats, then remove unavailable ones depending on the job status.
        output_mapping = {
            "tar.gz": os.path.join(
                model.runtime_environment_parameters[
                    str(RuntimeEnvironmentParameterName.S3_OUTPUT)
                ],
                model.job_id,
                "output",
                "output.tar.gz",
            ),
            "input": model.input_filename,
            "ipynb": (
                output_filename_parts[0].rstrip("-").replace(".", "-")
                + output_filename_parts[1]
            ),
            "log": "sagemaker_job_execution.log",
        }

        if model.status == Status.COMPLETED:
            # When we expand to more output formats, this should be updated to respect model.output_formats.
            return output_mapping

        (
            available_output_formats,
            _,
        ) = self.converter.determine_available_output_formats_and_failure_reason(
            model.status, training_job_response.get("FailureReason")
        )

        if not available_output_formats:
            # Allow the user to download only the original input file.
            return {
                "input": os.path.join(
                    model.runtime_environment_parameters[
                        str(RuntimeEnvironmentParameterName.S3_INPUT)
                    ].rstrip("/input"),
                    model.job_id,
                    "input",
                    model.input_filename,
                ),
            }

        available_output_formats.append("tar.gz")

        # Remove unavailable output formats.
        for output_format in [*output_mapping.keys()]:
            if output_format not in available_output_formats:
                output_mapping.pop(output_format, None)

        return output_mapping


class SageMakerStudioLabScheduler(SageMakerScheduler):
    # Scheduler that includes Studio Lab specific logic
    # Extends basic generic SageMaker scheduler

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.current_region = None

    def _reset_aws_clients(self):
        # Reset all cached clients, so they will get re-created next time
        # when they are used
        self._s3_client = None
        self._sagemaker_client = None
        self._event_bridge_client = None

    def sagemaker_client(self):
        region = get_region_name()

        # If the region we got differs from the region we used when creating
        # boto clients, it is likely customers changed their AWS config.
        # Reset and re-create those clients to avoid cached results.
        if self.current_region != region:
            self._reset_aws_clients()
            self.current_region = region

        if self._sagemaker_client is None:
            self._sagemaker_client = get_sagemaker_client()
        return self._sagemaker_client

    def s3_client(self):
        region = get_region_name()

        # If the region we got differs from the region we used when creating
        # boto clients, it is likely customers changed their AWS config.
        # Reset and re-create those clients to avoid cached results.
        if self.current_region != region:
            self._reset_aws_clients()
            self.current_region = region

        if self._s3_client is None:
            self._s3_client = get_s3_client()
        return self._s3_client

    def event_bridge_client(self):
        region = get_region_name()

        # If the region we got differs from the region we used when creating
        # boto clients, it is likely customers changed their AWS config.
        # Reset and re-create those clients to avoid cached results.
        if self.current_region != region:
            self._reset_aws_clients()
            self.current_region = region

        if self._event_bridge_client is None:
            self._event_bridge_client = get_event_bridge_client()
        return self._event_bridge_client

    def handle_aws_client_error(self, error, log_message=None):
        if self.error_matcher.is_expired_token_error(error):
            # If we got expired token error, reset all AWS clients to make sure
            # expired token are no longer cached, so clients will get new
            # credentials if customers refresh credentials on their own
            self._reset_aws_clients()
        super().handle_aws_client_error(error, log_message)

    def get_created_resources_description_text(self):
        return "Created for Notebook execution from Studio Lab"
