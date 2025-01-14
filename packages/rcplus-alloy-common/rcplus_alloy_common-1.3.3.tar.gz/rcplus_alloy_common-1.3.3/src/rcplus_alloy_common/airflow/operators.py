import re
from io import BytesIO
from urllib.parse import urlparse

import botocore
import boto3

from airflow.models import Variable, BaseOperator
from airflow.exceptions import AirflowException, AirflowSkipException
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.hooks.glue_catalog import GlueCatalogHook

from airflow.providers.amazon.aws.operators.ecs import EcsRunTaskOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.athena import AthenaOperator

from rcplus_alloy_common.airflow.hooks import SilentS3Hook
from rcplus_alloy_common.airflow.decorators import alloyize


@alloyize
class AlloyBashOperator(BashOperator):
    """Alloy BashOperator"""


@alloyize
class AlloyPythonOperator(PythonOperator):
    """Alloy PythonOperator"""


@alloyize
class AlloyGlueJobOperator(GlueJobOperator):
    """Alloy GlueJobOperator class with dag_run_id injected."""
    dest_s3_path = None
    logzio_appender_jar_s3_path = None
    job_default_args = None

    def get_job_default_args(self):
        if self.job_default_args is not None:
            return self.job_default_args
        boto3_session = boto3.Session()
        glue_client = boto3_session.client("glue")
        job = glue_client.get_job(JobName=self.job_name)
        if "Job" in job and "DefaultArguments" in job["Job"]:
            self.job_default_args = job["Job"]["DefaultArguments"]
        else:
            self.job_default_args = {}
        return self.job_default_args

    def prepare_log4j2(self, dag_id, dag_run_id):
        # retrieve the log4j2.properties S3 url and extract the bucket name and object key
        boto3_session = boto3.Session()
        ssm = boto3_session.client("ssm")
        conf_s3_path = ssm.get_parameter(Name="/alloy/airflow/glue/logzio_appender_conf_s3_path")["Parameter"]["Value"]
        self.logzio_appender_jar_s3_path = ssm.get_parameter(
            Name="/alloy/airflow/glue/logzio_appender_jarball_s3_path"
        )["Parameter"]["Value"]
        parsed_s3_url = urlparse(conf_s3_path, allow_fragments=False)
        s3_bucket_name = parsed_s3_url.netloc
        s3_key_src = parsed_s3_url.path.lstrip("/")
        #
        # read the log4j2.properties file from S3 as a template
        s3 = boto3_session.client("s3")
        templ = BytesIO()
        s3.download_fileobj(s3_bucket_name, s3_key_src, templ)
        #
        # inject the extra attributes into the template and upload the result back to S3
        extra_attrs = (
            f"env={self.project.get('env', 'dev')};"
            f"version={self.project.get('project_version', 'undefined')};"
            f"repository={self.project.get('git_repo_name', 'undefined')};"
            f"software_component={self.project.get('software_component', 'undefined')};"
            f"dag_id={dag_id or 'undefined'};"
            f"dag_run_id={dag_run_id or 'undefined'};"
            f"task_id={self.task_id or 'undefined'}"
        )
        conf_str_desc = re.sub(
            r"^appender\.logzio\.additionalFields\s*=\s*.*$",
            f"appender.logzio.additionalFields = {extra_attrs}",
            templ.getvalue().decode("utf-8"),
            flags=re.MULTILINE,
        )
        s3_key_dest = f"config/{dag_id}/{dag_run_id}/log4j2.properties"
        self.dest_s3_path = f"s3://{s3_bucket_name}/{s3_key_dest}"
        s3.upload_fileobj(BytesIO(conf_str_desc.encode("utf-8")), s3_bucket_name, s3_key_dest)

    def get_default_script_args(self, key):
        return self.get_job_default_args().get(key, None)

    def set_script_args(self, key, value):
        if key not in self.script_args:
            default_value = self.get_default_script_args(key)
            if default_value is not None:
                self.script_args[key] = default_value

        if key not in self.script_args:
            self.script_args[key] = value
        else:
            if value not in self.script_args[key].split(","):
                self.script_args[key] += f",{value}"

    def execute(self, context):
        # NOTE-zw: here we instruct the GlueJobOperator to use log4j2.properties from S3. This is a hack because there
        #         is no other way to pass the context attributes to log4j before it got initialized. The workaround we
        #         apply here is based on a BIG assumption: for each Glue Job run task there is a new Spark node
        #         initialized. This assumption is true for the current implementation of the GlueJobOperator as of
        #         2021-05-03 (Airflow 2.6.1).
        dag_id = context["dag"].dag_id
        dag_run_id = context["dag_run"].run_id
        self.prepare_log4j2(dag_id, dag_run_id)
        # self.set_script_args("--conf", f"spark.driver.extraJavaOptions=-Dlog4j.configurationFile={self.dest_s3_path}")
        self.set_script_args("--extra-files", self.dest_s3_path)
        self.set_script_args("--extra-jars", self.logzio_appender_jar_s3_path)
        return super().execute(context)


@alloyize
class AlloyEcsRunTaskOperator(EcsRunTaskOperator):
    """Alloy ECSRunTaskOperator"""

    def __init__(self, *args, cluster: str = "", overrides: dict | None = None, **kwargs):
        if overrides is None:
            overrides = {}
        super().__init__(*args, cluster=cluster, overrides=overrides, **kwargs)

    def set_cluster(self):
        if not self.cluster:
            self.cluster = Variable.get("global_SHARED_ECS_CLUSTER")

    def network_configuration_factory(self):
        self.network_configuration = {
            "awsvpcConfiguration": {
                "subnets": Variable.get("global_VPC_PRIVATE_SUBNETS").split(","),
                "securityGroups": [Variable.get("global_VPC_DEFAULT_SECURITY_GROUP")],
                "assignPublicIp": "DISABLED",
            },
        }

    def overrides_factory(self, dag_id, dag_run_id):
        # NOTE-zw:
        # We have to be very careful to handle the edge cases here, because:
        #   1. as an Alloy common practice, one ECS task normally contains two containers, one for the
        #      actual task and a sidecar for logging;
        #   2. `containerOverrides` might not exist
        #   3. the logger sidecar normally has no override in the definition (but it could have)
        #   4. `environment` might not exist
        if "containerOverrides" not in self.overrides:
            self.overrides["containerOverrides"] = []
        primary_container = None
        logging_sidecar = None
        for c in self.overrides["containerOverrides"]:
            # NOTE: the convention is that the primary container is named after the task definition
            if c["name"] == self.task_definition:
                # NOTE-zw: so far we do not have a reason to inject the logging context into the primary app container!
                primary_container = c
            elif c["name"] == "logzio-logs-router":
                # NOTE-zw: we need to inject the logging context into the logger sidecar because this is where the
                # fluent-bit runs.
                logging_sidecar = c
        if primary_container is None:
            if len(self.overrides["containerOverrides"]) > int(logging_sidecar is not None):
                additional_container_names = [
                    c["name"]
                    for c in self.overrides["containerOverrides"]
                    if c["name"] not in ["logzio-logs-router", self.task_definition]
                ]
                self.log.warning(
                    "containerOverrides contains containers other than "
                    f"['logzio-logs-router', '{self.task_definition}']: {additional_container_names}"
                )
            primary_container = {
                "name": self.task_definition,
                "environment": [],
            }
            self.overrides["containerOverrides"].append(primary_container)
        if logging_sidecar is None:
            if len(self.overrides["containerOverrides"]) > 1:
                additional_container_names = [
                    c["name"]
                    for c in self.overrides["containerOverrides"]
                    if c["name"] not in ["logzio-logs-router", self.task_definition]
                ]
                self.log.warning(
                    "containerOverrides contains containers other than "
                    f"['logzio-logs-router', '{self.task_definition}']: {additional_container_names}"
                )
            logging_sidecar = {
                "name": "logzio-logs-router",
                "environment": [],
            }
            self.overrides["containerOverrides"].append(logging_sidecar)
        if "environment" not in logging_sidecar:
            logging_sidecar["environment"] = []
        logging_sidecar["environment"].extend(
            [
                {"name": "DAG_RUN_ID", "value": dag_run_id},
                {"name": "DAG_ID", "value": dag_id},
                {"name": "TASK_ID", "value": self.task_id or "undefined"},
            ]
        )

    def execute(self, context, session=None):
        """
        Inject environment variables DAG_TASK_ID, DAG_RUN_ID, DAG_ID as logging context into both containers
        of the ECS task.
        The logging context helps to filter and locate log messages irrelevant from the original producer.
        """
        self.set_cluster()
        self.network_configuration_factory()
        self.overrides_factory(context["dag"].dag_id or "undefined", context["dag_run"].run_id or "undefined")

        return super().execute(context, session)


class S3ReleaseLockOperator(BaseOperator):
    """
    Custom class to handle S3-based locks release. The lock can be release only if a DAG "owns" the lock.
    The ownership is detected by lock's file content (lock_id).
    """

    def __init__(
        self,
        *,
        bucket: str,
        lock_key: str,
        lock_id: str,
        aws_conn_id: str = "aws_default",
        **kwargs,
    ):
        if any([bucket is None, lock_key is None, lock_id is None]):
            raise AirflowException("Bucket, lock_key and lock_id should not be None")

        super().__init__(**kwargs)
        self.bucket = bucket
        self.lock_key = lock_key
        self.lock_id = lock_id
        self.aws_conn_id = aws_conn_id

    def execute(self, context):
        s3_hook = S3Hook(aws_conn_id=self.aws_conn_id)
        try:
            lock_id = s3_hook.read_key(self.lock_key, self.bucket)
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                self.log.info(f"The lock `{self.lock_key}` does not exist")
                return
            raise e
        if lock_id == self.lock_id:
            self.log.info(f"Release the lock `{self.lock_key}`")
            s3_hook.delete_objects(bucket=self.bucket, keys=self.lock_key)
            return

        self.log.warning(
            f"The lock `{self.lock_key}` not released because its lock id is `{lock_id}` but expected `{self.lock_id}`"
        )


@alloyize
class AlloyS3ReleaseLockOperator(S3ReleaseLockOperator):
    """Alloy S3ReleaseLockOperator"""


@alloyize
class AlloyAthenaOperator(AthenaOperator):
    """Alloy AthenaOperator"""
    template_fields = tuple(AthenaOperator.template_fields) + ("workgroup", )


class AlloyAthenaOptimizeOperator(AlloyAthenaOperator):
    """
    The custom Athena operator to run and handle OPTIMIZE queries only. Any non-OPTIMIZE queries will be skipped.

    The current approach for the Athena Iceberg tables optimization:
    1) OPTIMIZE queries could fail so AWS recommends run them in the endless loop until the successful status.
    2) We run OPTIMIZE queries in loops for limited amount of rounds defined in self.max_optimization_rounds.
    3) If an OPTIMIZE query is successful AWS recommends run VACUUM query just after OPTIMIZE query and we do so.
    4) If an OPTIMIZE query fails we delete the table.
    5) If a VACUUM query fails we delete the table.
    6) To delete a table we do a two step process:
        1. delete table metadata from Glue data catalog
        2. delete table data files from S3
    7) After the optimization all dropped tables are re-created.
    """

    def __init__(
        self,
        *args,
        table_name: str,
        pre_hook=None,
        query=None,
        max_optimization_rounds=10,
        max_vacuum_rounds=10,
        **kwargs
    ):
        """

        Args:
            table_name (str)
                the table name to optimize
            pre_hook (str, optional)
                The pre-hook to run before the optimization. Defaults to None.
            query (str, optional)
                The optimization query to run. If None then the default query
                ```f"OPTIMIZE {table_name} REWRITE DATA USING BIN_PACK"```
                will be used. Defaults to None.
            max_optimization_rounds (int, optional)
                Maximum number of OPTIMIZE rounds to run. Defaults to 10.
            max_vacuum_rounds (int, optional):
                Maximum number of VACUUM rounds to run. Defaults to 10.
        """
        assert table_name is not None, "table_name is required"

        if query is None:
            self.optimize_query = f"OPTIMIZE {table_name} REWRITE DATA USING BIN_PACK"
        else:
            self.log.warning(f"execute {query} instead of default OPTIMIZE query for table `{table_name}`")
            self.optimize_query = query
        super().__init__(
            *args,
            query=pre_hook,
            project_depth=6,
            **kwargs
        )
        self.table_name = table_name
        self.optimization_round = 1
        self.max_optimization_rounds = max_optimization_rounds
        self.max_vacuum_rounds = max_vacuum_rounds
        self.vacuum_round = 1

    def _optimize(self, context):
        self.query = self.optimize_query
        while self.optimization_round <= self.max_optimization_rounds:
            try:
                self.log.info(
                    f"Perform optimization round {self.optimization_round}. Execute {self.query}"
                )
                super().execute(context)
                return True
            except Exception as ex:  # pylint: disable=broad-except
                if "ICEBERG_OPTIMIZE_MORE_RUNS_NEEDED" in str(ex):
                    self.log.info(f"Failed to execute `{self.query}` because of `{ex}`.")
                    self.optimization_round += 1
                    continue

                self.log.error(f"Failed to execute {self.query}", exc_info=True)
                return False
        return False

    def _vacuum(self, context):
        # VACUUM also could require to perform several rounds
        self.query = f"VACUUM {self.table_name}"
        while self.vacuum_round <= self.max_vacuum_rounds:
            try:
                self.log.info(
                    f"Perform vacuum round {self.vacuum_round}. Execute {self.query}"
                )
                super().execute(context)
                return True
            except Exception as ex:  # pylint: disable=broad-except
                if "ICEBERG_VACUUM_MORE_RUNS_NEEDED" in str(ex):
                    self.log.info(
                        f"Failed to execute `{self.query}` because of `{ex}`."
                    )
                    self.vacuum_round += 1
                    continue

                self.log.error(f"Failed to execute {self.query}", exc_info=True)
                return False
        return False

    def _drop_table(self):
        glue_hook = GlueCatalogHook()
        # delete table metadata from Glue data catalog
        table_location = glue_hook.get_table_location(
            database_name=self.database,
            table_name=self.table_name,
        )
        glue_hook.get_conn().delete_table(
            DatabaseName=self.database,
            Name=self.table_name,
        )

        s3_hook = SilentS3Hook()
        self.log.info(f"Clean S3 {table_location} prefix.")
        bucket_name = table_location.split("/")[2]
        s3_prefix = "/".join(table_location.split("/")[3:])
        s3_files = s3_hook.list_keys(bucket_name=bucket_name, prefix=s3_prefix)
        s3_hook.delete_objects(bucket=bucket_name, keys=s3_files)

    def execute(self, context):
        if self.query is not None:
            self.log.info(f"Run pre-hook {self.query}")
            super().execute(context)

        optimization_ok = self._optimize(context)

        if optimization_ok:
            optimization_ok = self._vacuum(context)

        if not optimization_ok:
            self._drop_table()


class AlloyDbtEcsRunTaskOperator(AlloyEcsRunTaskOperator):
    """
    The custom EcsRunTaskOperator to execute a DBT command to refresh DBT models if required
    """
    TABLES_PLACEHOLDER = "__TABLES_PLACEHOLDER__"

    template_fields = tuple(AlloyEcsRunTaskOperator.template_fields) + (
        "database",
    )

    def __init__(
        self,
        *args,
        task_definition,
        database: str,
        table_names: list[str],
        **kwargs,
    ):
        default_command = [
            "dbt",
            "run",
            "--full-refresh",
            "-m",
            self.TABLES_PLACEHOLDER,  # will be replaced with a list of tables
            "--profiles-dir",
            ".",
        ]
        default_overrides = {
            "containerOverrides": [
                {
                    "name": task_definition,
                    "command": default_command,
                },
            ],
        }
        overrides = kwargs.pop("overrides", {})
        if not overrides:
            overrides = default_overrides
        else:
            cmd_patched = False
            for container in overrides["containerOverrides"]:
                if container["name"] == task_definition:
                    if "command" in container:
                        self.log.warning(
                            f"The container command {container['command']} will be replaced with {default_command}"
                        )
                    container["command"] = default_command
                    cmd_patched = True
                    break

            if not cmd_patched:
                raise AirflowException(
                    f"no container with name {task_definition} found in overrides"
                )

        super().__init__(
            *args,
            task_definition=task_definition,
            overrides=overrides,
            project_depth=6,
            **kwargs
        )
        self.database = database
        self.table_names = table_names

    def get_refresh_tables(self):
        glue_hook = GlueCatalogHook()
        response = glue_hook.get_conn().get_tables(
            DatabaseName=self.database, Expression="|".join(self.table_names)
        )
        refresh_tables = []
        available_tables = [table["Name"] for table in response["TableList"]]
        for table_name in self.table_names:
            if table_name not in available_tables:
                refresh_tables.append(table_name)
        return refresh_tables

    def _update_command(self, table_names):
        for container in self.overrides["containerOverrides"]:
            if container["name"] == self.task_definition:
                command = container["command"]
        for table_name in table_names:
            command.insert(command.index(self.TABLES_PLACEHOLDER), table_name)
        command.remove(self.TABLES_PLACEHOLDER)

    def execute(self, context, session=None):
        refresh_tables = self.get_refresh_tables()
        if not refresh_tables:
            raise AirflowSkipException("No tables to refresh")
        self._update_command(refresh_tables)
        self.log.info(f"Tables to refresh {refresh_tables}")
        super().execute(context, session)
