import base64
import configparser
import logging
import os
import pathlib
from datetime import timedelta
from netrc import netrc
from platform import system
from typing import Literal, Optional, Tuple

import click
import lxml.html
import requests
from cachier import cachier

from copernicus_marine_client.core_functions.utils import (
    DEFAULT_CLIENT_BASE_DIRECTORY,
)

DEFAULT_CLIENT_CREDENTIALS_FILENAME = ".copernicus-marine-credentials"
DEFAULT_CLIENT_CREDENTIALS_FILEPATH = (
    DEFAULT_CLIENT_BASE_DIRECTORY / DEFAULT_CLIENT_CREDENTIALS_FILENAME
)


class CredentialCannotBeNone(Exception):
    ...


class IncorrectUsernameOrPassword(Exception):
    ...


def _load_credential_from_copernicus_marine_configuration_file(
    credential_type: Literal["username", "password"],
    configuration_filename: pathlib.Path,
) -> Optional[str]:
    configuration_file = open(configuration_filename)
    configuration_string = base64.standard_b64decode(
        configuration_file.read()
    ).decode("utf8")
    config = configparser.RawConfigParser()
    config.read_string(configuration_string)
    credential = config.get("credentials", credential_type)
    if credential:
        logging.debug(
            f"{credential_type} loaded from {configuration_filename}"
        )
    return credential


def _load_credential_from_netrc_configuration_file(
    credential_type: Literal["username", "password"],
    configuration_filename: pathlib.Path,
    host: str,
) -> Optional[str]:
    authenticator = netrc(configuration_filename).authenticators(host=host)
    if authenticator:
        username, _, password = authenticator
        logging.debug(
            f"{credential_type} loaded from {configuration_filename}"
        )
        return username if credential_type == "username" else password
    else:
        return None


def _load_credential_from_motu_configuration_file(
    credential_type: Literal["username", "password"],
    configuration_filename: pathlib.Path,
) -> Optional[str]:
    motu_file = open(configuration_filename)
    motu_credential_type = "user" if credential_type == "username" else "pwd"
    config = configparser.RawConfigParser()
    config.read_string(motu_file.read())
    credential = config.get("Main", motu_credential_type)
    if credential:
        logging.debug(
            f"{credential_type} loaded from {configuration_filename}"
        )
    return credential


def _retrieve_credential_from_prompt(
    credential_type: Literal["username", "password"], hide_input: bool
) -> str:
    return click.prompt(credential_type, hide_input=hide_input)


def _retrieve_credential_from_environment_variable(
    credential_type: Literal["username", "password"]
) -> Optional[str]:
    if credential_type == "username":
        return os.getenv("COPERNICUS_MARINE_SERVICE_USERNAME")
    if credential_type == "password":
        return os.getenv("COPERNICUS_MARINE_SERVICE_PASSWORD")
    return None


def _retrieve_credential_from_custom_configuration_files(
    credential_type: Literal["username", "password"],
    credentials_file: pathlib.Path,
    host: str = "default_host",
) -> Optional[str]:
    credential = _load_credential_from_copernicus_marine_configuration_file(
        credential_type, credentials_file
    )
    if not credential:
        credential = _load_credential_from_motu_configuration_file(
            credential_type, credentials_file
        )
        if not credential:
            credential = _load_credential_from_netrc_configuration_file(
                credential_type, credentials_file, host=host
            )
    return credential


def _retrieve_credential_from_default_configuration_files(
    credential_type: Literal["username", "password"],
    host: str = "default_host",
) -> Optional[str]:
    copernicus_marine_configuration_file = pathlib.Path(
        DEFAULT_CLIENT_CREDENTIALS_FILEPATH
    )
    motu_configuration_file = pathlib.Path(
        pathlib.Path.home() / "motuclient" / "motuclient-python.ini"
    )
    netrc_configuration_file = pathlib.Path(
        pathlib.Path.home() / ("_netrc" if system() == "Windows" else ".netrc")
    )
    if copernicus_marine_configuration_file.exists():
        credential = (
            _load_credential_from_copernicus_marine_configuration_file(
                credential_type,
                copernicus_marine_configuration_file,
            )
        )
    elif motu_configuration_file.exists():
        credential = _load_credential_from_motu_configuration_file(
            credential_type, motu_configuration_file
        )
    elif netrc_configuration_file.exists():
        credential = _load_credential_from_netrc_configuration_file(
            credential_type, netrc_configuration_file, host=host
        )
    else:
        credential = None
    return credential


def _retrieve_credential_from_configuration_files(
    credential_type: Literal["username", "password"],
    credentials_file: Optional[pathlib.Path],
    host: str = "default_host",
) -> Optional[str]:
    if credentials_file and credentials_file.exists():
        credential = _retrieve_credential_from_custom_configuration_files(
            credential_type, credentials_file, host
        )
    else:
        credential = _retrieve_credential_from_default_configuration_files(
            credential_type, host
        )
    return credential


def create_copernicus_marine_client_configuration_file(
    username: str,
    password: str,
    configuration_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
) -> pathlib.Path:
    configuration_lines = [
        "[credentials]\n",
        f"username={username}\n",
        f"password={password}\n",
    ]
    configuration_filename = pathlib.Path(
        configuration_file_directory / DEFAULT_CLIENT_CREDENTIALS_FILENAME
    )
    if configuration_filename.exists() and not overwrite_configuration_file:
        click.confirm(
            f"File {configuration_filename} already exists, overwrite it ?",
            abort=True,
        )
    configuration_file_directory.mkdir(parents=True, exist_ok=True)
    configuration_file = open(configuration_filename, "w")
    configuration_string = base64.b64encode(
        "".join(configuration_lines).encode("ascii", "strict")
    ).decode("utf8")
    configuration_file.write(configuration_string)
    configuration_file.close()
    return configuration_filename


@cachier(stale_after=timedelta(hours=5))
def _are_copernicus_marine_credentials_valid(
    username: str, password: str
) -> bool:
    """
    Check provided Copernicus Marine Credentials are correct.

    Parameters
    ----------
    username : str
        Copernicus Marine Username, provided for free from https://marine.copernicus.eu
    password : str
        Copernicus Marine Password, provided for free from https://marine.copernicus.eu

    """
    cmems_cas_url = "https://cmems-cas.cls.fr/cas/login"
    conn_session = requests.session()
    login_session = conn_session.get(cmems_cas_url)
    login_from_html = lxml.html.fromstring(login_session.text)
    hidden_elements_from_html = login_from_html.xpath(
        '//form//input[@type="hidden"]'
    )
    playload = {
        he.attrib["name"]: he.attrib["value"]
        for he in hidden_elements_from_html
    }
    playload["username"] = username
    playload["password"] = password
    response = conn_session.post(cmems_cas_url, data=playload)
    return response.text.find("success") != -1


def get_credential(
    credential: Optional[str],
    credential_type: Literal["username", "password"],
    hide_input: bool,
    credentials_file: Optional[pathlib.Path],
) -> str:
    if not credential:
        credential = _retrieve_credential_from_environment_variable(
            credential_type
        )
        if not credential:
            credential = _retrieve_credential_from_configuration_files(
                credential_type=credential_type,
                credentials_file=credentials_file,
                host="my.cmems-du.eu",
            )
            if not credential:
                credential = _retrieve_credential_from_prompt(
                    credential_type, hide_input=hide_input
                )
                if not credential:
                    raise ValueError(f"{credential} cannot be None")
    else:
        logging.debug(
            "Credentials loaded from function arguments or environment variable"
        )
    return credential


def get_and_check_username_password(
    username: Optional[str],
    password: Optional[str],
    credentials_file: Optional[pathlib.Path],
) -> Tuple[str, str]:
    username, password = get_username_password(
        username=username, password=password, credentials_file=credentials_file
    )
    copernicus_marine_credentials_are_valid = (
        _are_copernicus_marine_credentials_valid(username, password)
    )
    if not copernicus_marine_credentials_are_valid:
        raise IncorrectUsernameOrPassword(
            "Learn how to recover your credentials at: "
            "https://help.marine.copernicus.eu/en/articles/"
            "4444552-i-forgot-my-username-or-my-password-what-should-i-do"
        )
    return (username, password)


def get_username_password(
    username: Optional[str],
    password: Optional[str],
    credentials_file: Optional[pathlib.Path],
) -> Tuple[str, str]:
    username = get_credential(
        username,
        "username",
        hide_input=False,
        credentials_file=credentials_file,
    )
    password = get_credential(
        password,
        "password",
        hide_input=True,
        credentials_file=credentials_file,
    )
    return (username, password)


def _get_credential_from_environment_variable_or_prompt(
    credential: Optional[str],
    credential_type: Literal["username", "password"],
    hide_input: bool,
) -> str:
    if not credential:
        credential = _retrieve_credential_from_environment_variable(
            credential_type
        )
        if not credential:
            credential = _retrieve_credential_from_prompt(
                credential_type, hide_input
            )
            if not credential:
                raise CredentialCannotBeNone(credential_type)
    return credential


def credentials_file_builder(
    username: Optional[str],
    password: Optional[str],
    configuration_file_directory: pathlib.Path,
    overwrite_configuration_file: bool,
) -> Optional[pathlib.Path]:
    username = _get_credential_from_environment_variable_or_prompt(
        username, "username", False
    )
    password = _get_credential_from_environment_variable_or_prompt(
        password, "password", True
    )
    copernicus_marine_credentials_are_valid = (
        _are_copernicus_marine_credentials_valid(username, password)
    )
    if copernicus_marine_credentials_are_valid:
        configuration_file = (
            create_copernicus_marine_client_configuration_file(
                username=username,
                password=password,
                configuration_file_directory=configuration_file_directory,
                overwrite_configuration_file=overwrite_configuration_file,
            )
        )
        return configuration_file
    return None
