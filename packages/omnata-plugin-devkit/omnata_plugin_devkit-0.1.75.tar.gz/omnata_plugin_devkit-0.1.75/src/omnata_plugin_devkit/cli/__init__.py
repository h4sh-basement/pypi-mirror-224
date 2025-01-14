from pathlib import Path
import typer
import click
from snowcli import config
from ..plugin_uploader import PluginUploader
from ..native_app_packaging import NativeAppPackaging
from ..initialiser import new_plugin_generator
from ..plugin_registration import PluginRegistration

# class PrescribedOrderGroup(click.Group):
#    def list_commands(self, ctx):
#        return ['init', 'upload', 'deploy', 'register']

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})


@app.command()
def init():
    """
    Generates a template for a new plugin, into the current directory.
    """
    new_plugin_generator()


@app.command()
def upload(
    plugin_path: Path = typer.Option(".", "--plugin_path", "-p", help="Plugin Path"),
    target_database: str = typer.Option(
        "OMNATA_PLUGIN_DEVELOPMENT",
        "-d",
        "--database",
        help="The database to create the plugin in",
    ),
    target_schema: str = typer.Option(
        None,
        "-s",
        "--schema",
        help="The schema to create the plugin in. If not provided, the uppercased plugin_id from the manifest will be used",
    ),
    target_stage: str = typer.Option(
        "PLUGIN_CODE", "--target_stage", help="The stage to copy to plugin code into"
    ),
    package_name: str = typer.Option(
        None,
        "-n",
        "--package_name",
        help='The name of the application package to create/update. If not provided, the schema name will be used, with "_PLUGIN" appended',
    ),
    package_version: str = typer.Option(
        "DEVELOPMENT",
        "--package_version",
        help="Name of application package version to create/update",
    ),
    developer_role: str = typer.Option(
        None,
        "--developer_role",
        help="Name of role to grant DEVELOP access on the package, which determines who has access to debug mode",
    ),
    environment: str = typer.Option(
        "dev",
        "-e",
        "--environment",
        help="Name of environment (e.g. dev, prod, staging), this is used to obtain snowcli credentials",
    ),
    airbyte: bool = typer.Option(
        False,
        "--airbyte",
        help="EXPERIMENTAL: Attempt to wrap and upload an Airbyte connector developed with the Python CDK. The plugin_path parameter should contain a source.py file.",
    ),
):
    """
    Packages a plugin directory, uploads to a Snowflake stage and creates an Application Package.
    """

    snowflake_connector = config.connect_to_snowflake(connection_name=environment)
    uploader = PluginUploader(snowflake_connection=snowflake_connector.ctx)
    target_schema = uploader.upload_plugin(
        plugin_directory=plugin_path.resolve(),
        database_name=target_database,
        schema_name=target_schema,
        stage_name=target_stage,
        is_airbyte=airbyte,
    )
    if package_name is None:
        package_name = target_schema + "_PLUGIN"
    packager = NativeAppPackaging(
        snowflake_connection=snowflake_connector.ctx,
        package_name=package_name,
    )
    packager.create_package(developer_role=developer_role)
    patch_number = packager.create_package_version(
        code_database=target_database,
        code_schema=target_schema,
        code_stage=target_stage,
        version_name=package_version,
    )
    print(
        f"Successfully uploaded plugin {package_name}, version {package_version}, patch {patch_number}"
    )


@app.command()
def deploy(
    package_name: str = typer.Argument(
        ..., help="The name of the application package to deploy (from upload command)"
    ),
    application_name: str = typer.Argument(
        ..., help="The name of the application to deploy from the package"
    ),
    package_version: str = typer.Option(
        "DEVELOPMENT",
        "--package_version",
        help="Name of application package version to deploy",
    ),
    package_patch_version: int = typer.Option(
        None,
        help="The patch number to use, if not specified the latest patch will be used",
    ),
    environment: str = typer.Option(
        "dev",
        "-e",
        "--environment",
        help="Name of environment (e.g. dev, prod, staging)",
    ),
):
    """
    Creates a plugin Application from an uploaded Application package.
    """
    snowflake_connector = config.connect_to_snowflake(connection_name=environment)
    packager = NativeAppPackaging(
        snowflake_connection=snowflake_connector.ctx,
        package_name=package_name,
    )
    created = packager.deploy_application(
        application_name=application_name,
        version_name=package_version,
        patch_number=package_patch_version,
    )
    if created:
        print(
            f"Successfully deployed new application {application_name}, version {package_version}"
        )
    else:
        if package_patch_version:
            print(
                f"Application {application_name} updated to patch {package_patch_version} of version {package_version}"
            )
        else:
            print(
                f"Application {application_name} updated to latest patch of version {package_version}"
            )


@app.command()
def register(
    plugin_application_name: str = typer.Argument(
        ..., help="The name of the plugin application"
    ),
    omnata_application_name: str = typer.Argument(
        "OMNATA",
        help="The name of the Omnata Application (default of OMNATA per marketplace listing installation)",
    ),
    environment: str = typer.Option(
        "dev",
        "-e",
        "--environment",
        help="Name of environment (e.g. dev, prod, staging)",
    ),
):
    """
    Registers a deployed plugin Application with the Omnata Application.
    """
    snowflake_connector = config.connect_to_snowflake(connection_name=environment)
    registerer = PluginRegistration(snowflake_connection=snowflake_connector.ctx)
    registerer.register_plugin(
        plugin_application_name=plugin_application_name,
        omnata_application_name=omnata_application_name,
    )


def check_env_conf(env_conf, environment):
    if env_conf is None:
        print(
            f"The {environment} environment is not configured in app.toml "
            f"yet, please run `snow configure {environment}` first before continuing.",
        )
        raise typer.Abort()
