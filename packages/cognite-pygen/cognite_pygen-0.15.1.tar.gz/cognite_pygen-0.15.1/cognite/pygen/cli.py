from pathlib import Path
from typing import Annotated, cast

from cognite.client import CogniteClient
from cognite.client.exceptions import CogniteAPIError

from cognite import pygen
from cognite.pygen._generator import generate_sdk
from cognite.pygen._settings import PygenSettings, load_settings

try:
    import typer
except ImportError:
    _has_typer = False
else:
    _has_typer = True


def _version_callback(value: bool):
    if value:
        typer.echo(pygen.__version__)
        raise typer.Exit()


if _has_typer:
    app = typer.Typer(add_completion=False)

    @app.callback()
    def common(
        ctx: typer.Context,
        version: bool = typer.Option(None, "--version", callback=_version_callback),
    ):
        ...

    settings = load_settings()
    help_text = "Generate a Python SDK from Data Model(s)"
    if settings is not None:
        loaded_settings = cast(PygenSettings, settings)

        @app.command(help=help_text)
        def generate(
            client_secret: Annotated[str, typer.Option(..., help="Azure Client Secret for connecting to CDF")],
            space: str = typer.Option(default=loaded_settings.space.default, help=loaded_settings.space.help),
            external_id: str = typer.Option(
                default=loaded_settings.external_id.default, help=loaded_settings.external_id.help
            ),
            version: str = typer.Option(default=loaded_settings.version.default, help=loaded_settings.version.help),
            tenant_id: str = typer.Option(
                default=loaded_settings.tenant_id.default, help=loaded_settings.tenant_id.help
            ),
            client_id: str = typer.Option(
                default=loaded_settings.client_id.default, help=loaded_settings.client_id.help
            ),
            cdf_cluster: str = typer.Option(
                default=loaded_settings.cdf_cluster.default, help=loaded_settings.cdf_cluster.help
            ),
            cdf_project: str = typer.Option(
                default=loaded_settings.cdf_project.default, help=loaded_settings.cdf_project.help
            ),
            output_dir: Path = typer.Option(
                default=loaded_settings.output_dir.default or Path.cwd(), help=loaded_settings.output_dir.help
            ),
            top_level_package: str = typer.Option(
                loaded_settings.top_level_package.default, help=loaded_settings.top_level_package.help
            ),
            client_name: str = typer.Option(loaded_settings.client_name.default, help=loaded_settings.client_name.help),
        ):
            client = CogniteClient.default_oauth_client_credentials(
                cdf_project, cdf_cluster, tenant_id, client_id, client_secret
            )
            try:
                generate_sdk(
                    client, (space, external_id, version), top_level_package, client_name, output_dir, typer.echo
                )
            except (CogniteAPIError, IndexError) as e:
                raise typer.Exit(code=1) from e

    else:
        default_settings = PygenSettings()

        @app.command(help=help_text)
        def generate(
            space: Annotated[str, typer.Option(..., help=default_settings.space.help)],
            external_id: Annotated[str, typer.Option(..., help=default_settings.external_id.help)],
            version: Annotated[str, typer.Option(..., help=default_settings.version.help)],
            tenant_id: Annotated[str, typer.Option(..., help=default_settings.tenant_id.help)],
            client_id: Annotated[str, typer.Option(..., help=default_settings.client_id.help)],
            client_secret: Annotated[str, typer.Option(..., help="Azure Client Secret for connecting to CDF")],
            cdf_cluster: Annotated[str, typer.Option(..., help=default_settings.cdf_cluster.help)],
            cdf_project: Annotated[str, typer.Option(..., help=default_settings.cdf_project.help)],
            output_dir: Path = typer.Option(Path.cwd(), help=default_settings.output_dir.help),
            top_level_package: str = typer.Option(
                default_settings.top_level_package.default, help=default_settings.top_level_package.help
            ),
            client_name: str = typer.Option(
                default_settings.client_name.default, help=default_settings.client_name.help
            ),
        ):
            client = CogniteClient.default_oauth_client_credentials(
                cdf_project, cdf_cluster, tenant_id, client_id, client_secret
            )
            try:
                generate_sdk(
                    client, (space, external_id, version), top_level_package, client_name, output_dir, typer.echo
                )
            except (CogniteAPIError, IndexError) as e:
                raise typer.Exit(code=1) from e

    def main():
        app()

else:

    def main():
        print("THE CLI requires typer to be available, install with `pip install cognite-pygen[cli]")


if __name__ == "__main__":
    main()
