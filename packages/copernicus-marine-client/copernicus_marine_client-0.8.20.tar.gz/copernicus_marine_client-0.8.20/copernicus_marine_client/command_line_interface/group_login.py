import logging
import logging.config
import pathlib
from typing import Optional

import click

from copernicus_marine_client.core_functions.credentials_utils import (
    credentials_file_builder,
)
from copernicus_marine_client.core_functions.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
)


@click.group()
def cli_group_login() -> None:
    pass


@cli_group_login.command(
    "login",
    short_help="Login to the Copernicus Marine Service",
    help="""
    Login to the Copernicus Marine Service.

    Create a configuration file under the $HOME/.copernicus_marine_client directory (overwritable with option --credentials-file).
    """,  # noqa
    epilog="""
    Examples:

    \b
    COPERNICUS_MARINE_SERVICE_USERNAME=<USERNAME> COPERNICUS_MARINE_SERVICE_PASSWORD=<PASSWORD> copernicus-marine login

    \b
    copernicus-marine login --username <USERNAME> --password <PASSWORD>

    \b
    copernicus-marine login
    > Username: [USER-INPUT]
    > Password: [USER-INPUT]
    """,  # noqa
)
@click.option(
    "--username",
    prompt="username",
    hide_input=False,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_USERNAME"
    + ", or else ask for user input",
)
@click.option(
    "--password",
    prompt="password",
    hide_input=True,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_PASSWORD"
    + ", or else ask for user input",
)
@click.option(
    "--configuration-file-directory",
    type=click.Path(path_type=pathlib.Path),
    default=DEFAULT_CLIENT_BASE_DIRECTORY,
    help="Path to the directory where the configuration file is stored",
)
@click.option(
    "--overwrite-configuration-file",
    "-overwrite",
    is_flag=True,
    default=False,
    help="Flag to skip confirmation before overwriting configuration file",
)
@click.option(
    "--verbose",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL", "QUIET"]),
    default="INFO",
    help=(
        "Set the details printed to console by the command "
        "(based on standard logging library)."
    ),
)
def login(
    username: Optional[str],
    password: Optional[str],
    configuration_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
    verbose: str = "INFO",
) -> None:
    if verbose == "QUIET":
        logging.root.disabled = True
        logging.root.setLevel(level="CRITICAL")
    else:
        logging.root.setLevel(level=verbose)
    credentials_file = credentials_file_builder(
        username=username,
        password=password,
        configuration_file_directory=configuration_file_directory,
        overwrite_configuration_file=overwrite_configuration_file,
    )
    if credentials_file is not None:
        logging.info(f"Credentials file stored in {credentials_file}.")
    else:
        logging.info(
            "Invalid credentials. No configuration file have been modified."
        )
        logging.info(
            "Learn how to recover your credentials at: "
            "https://help.marine.copernicus.eu/en/articles/"
            "4444552-i-forgot-my-username-or-my-password-what-should-i-do"
        )


if __name__ == "__main__":
    cli_group_login()
