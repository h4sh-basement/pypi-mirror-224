import logging
import logging.config
import pathlib
from datetime import datetime
from typing import List, Optional

import click

from copernicus_marine_client.command_line_interface.exception_handler import (
    log_exception_and_exit,
)
from copernicus_marine_client.command_line_interface.utils import (
    MutuallyExclusiveOption,
)
from copernicus_marine_client.core_functions.services_utils import CommandType
from copernicus_marine_client.core_functions.subset import subset_function
from copernicus_marine_client.core_functions.utils import (
    OVERWRITE_LONG_OPTION,
    OVERWRITE_OPTION_HELP_TEXT,
    OVERWRITE_SHORT_OPTION,
)


@click.group()
def cli_group_subset() -> None:
    pass


@cli_group_subset.command(
    "subset",
    short_help="Download subsets of datasets as NetCDF files or Zarr stores",
    help="""
    Download subsets of datasets as NetCDF files or Zarr stores.

    Either one of --dataset-id or --dataset-url is required (can be found via the "describe" command).
    The arguments value passed individually through the CLI take precedence over the values from the --motu-api-request option,
    which takes precedence over the ones from the --request-file option
    """,  # noqa
    epilog="""
    Examples:

    \b
    copernicus-marine subset
    --dataset-id METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2
    --variable analysed_sst --variable sea_ice_fraction
    --start-datetime 2021-01-01 --end-datetime 2021-01-02
    --minimal-longitude 0.0 --maximal-longitude 0.1
    --minimal-latitude 0.0 --maximal-latitude 0.1

    \b
    copernicus-marine subset -i METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 -T 2021-01-02 -x 0.0 -X 0.1 -y 0.0 -Y 0.1
    """,  # noqa
)
@click.option(
    "--dataset-url",
    "-u",
    type=str,
    help="The full dataset URL.",
)
@click.option(
    "--dataset-id",
    "-i",
    type=str,
    help="The dataset id.",
)
@click.option(
    "--username",
    type=str,
    default=None,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_USERNAME"
    + ", or else look for configuration files, or else ask for user input.",
)
@click.option(
    "--password",
    type=str,
    default=None,
    help="If not set, search for environment variable"
    + " COPERNICUS_MARINE_SERVICE_PASSWORD"
    + ", or else look for configuration files, or else ask for user input.",
)
@click.option(
    "--variable",
    "-v",
    "variables",
    type=str,
    help="Specify dataset variables",
    multiple=True,
)
@click.option(
    "--minimal-longitude",
    "-x",
    type=float,
    help=(
        "Minimal longitude for the subset. "
        "The value will be reduced to the interval [-180; 360[."
    ),
)
@click.option(
    "--maximal-longitude",
    "-X",
    type=float,
    help=(
        "Maximal longitude for the subset. "
        "The value will be reduced to the interval [-180; 360[."
    ),
)
@click.option(
    "--minimal-latitude",
    "-y",
    type=click.FloatRange(min=-90, max=90),
    help="Minimal latitude for the subset. Requires a float within this range:",
)
@click.option(
    "--maximal-latitude",
    "-Y",
    type=click.FloatRange(min=-90, max=90),
    help="Maximal latitude for the subset. Requires a float within this range:",
)
@click.option(
    "--minimal-depth",
    "-z",
    type=click.FloatRange(min=0),
    help="Minimal depth for the subset. Requires a float within this range:",
)
@click.option(
    "--maximal-depth",
    "-Z",
    type=click.FloatRange(min=0),
    help="Maximal depth for the subset. Requires a float within this range:",
)
@click.option(
    "--vertical-dimension-as-originally-produced",
    type=bool,
    default=True,
    show_default=True,
    help=(
        "Consolidate the vertical dimension (the z-axis) as it is in the "
        "dataset originally produced, "
        "named `depth` with descending positive values."
    ),
)
@click.option(
    "--start-datetime",
    "-t",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The start datetime of the temporal subset. Caution: encapsulate date "
    + 'with " " to ensure valid expression for format "%Y-%m-%d %H:%M:%S".',
)
@click.option(
    "--end-datetime",
    "-T",
    type=click.DateTime(
        ["%Y", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    ),
    help="The end datetime of the temporal subset. Caution: encapsulate date "
    + 'with " " to ensure valid expression for format "%Y-%m-%d %H:%M:%S".',
)
@click.option(
    "--output-directory",
    "-o",
    type=click.Path(path_type=pathlib.Path),
    help="The destination folder for the downloaded files."
    + " Default is the current directory.",
)
@click.option(
    "--credentials-file",
    type=click.Path(path_type=pathlib.Path),
    help=(
        "Path to a credentials file if not in its default directory. "
        "Accepts .copernicus-marine-credentials / .netrc or _netrc / "
        "motuclient-python.ini files."
    ),
)
@click.option(
    "--output-filename",
    "-f",
    type=click.Path(path_type=pathlib.Path),
    help=(
        "Concatenate the downloaded data in the given file name "
        "(under the output directory). If "
        "the output-filename argument ends with '.nc' suffix, the file will be "
        "downloaded as a netCDF file."
    ),
)
@click.option(
    "--force-download",
    is_flag=True,
    default=False,
    help="Flag to skip confirmation before download.",
)
@click.option(
    OVERWRITE_LONG_OPTION,
    OVERWRITE_SHORT_OPTION,
    is_flag=True,
    default=False,
    help=OVERWRITE_OPTION_HELP_TEXT,
)
@click.option(
    "--force-service",
    "-s",
    type=str,
    help=(
        "Force download through one of the available services "
        f"using the service name among {CommandType.SUBSET.service_names()} "
        f"or its short name among {CommandType.SUBSET.service_short_names()}."
    ),
)
@click.option(
    "--request-file",
    type=click.Path(exists=True, path_type=pathlib.Path),
    help="Option to pass a file containing CLI arguments. "
    "The file MUST follow the structure of dataclass 'SubsetRequest'.",
)
@click.option(
    "--motu-api-request",
    type=str,
    help=(
        "Option to pass a complete MOTU api request as a string. "
        'Caution, user has to replace double quotes " with single '
        "quotes ' in the request."
    ),
)
@click.option(
    "--overwrite-metadata-cache",
    cls=MutuallyExclusiveOption,
    type=bool,
    is_flag=True,
    default=False,
    help="Force to refresh the catalogue by overwriting the local cache.",
    mutually_exclusive=["no_metadata_cache"],
)
@click.option(
    "--no-metadata-cache",
    cls=MutuallyExclusiveOption,
    type=bool,
    is_flag=True,
    default=False,
    help="Bypass the use of cache.",
    mutually_exclusive=["overwrite_metadata_cache"],
)
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL", "QUIET"]),
    default="INFO",
    help=(
        "Set the details printed to console by the command "
        "(based on standard logging library)."
    ),
)
@log_exception_and_exit
def subset(
    dataset_url: Optional[str],
    dataset_id: Optional[str],
    username: Optional[str],
    password: Optional[str],
    variables: Optional[List[str]],
    minimal_longitude: Optional[float],
    maximal_longitude: Optional[float],
    minimal_latitude: Optional[float],
    maximal_latitude: Optional[float],
    minimal_depth: Optional[float],
    maximal_depth: Optional[float],
    vertical_dimension_as_originally_produced: bool,
    start_datetime: Optional[datetime],
    end_datetime: Optional[datetime],
    output_filename: Optional[pathlib.Path],
    force_service: Optional[str],
    request_file: Optional[pathlib.Path],
    output_directory: Optional[pathlib.Path],
    credentials_file: Optional[pathlib.Path],
    motu_api_request: Optional[str],
    force_download: bool,
    overwrite_output_data: bool,
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
    log_level: str,
):
    if log_level == "QUIET":
        logging.root.disabled = True
        logging.root.setLevel(level="CRITICAL")
    else:
        logging.root.setLevel(level=log_level)

    subset_function(
        dataset_url,
        dataset_id,
        username,
        password,
        variables,
        minimal_longitude,
        maximal_longitude,
        minimal_latitude,
        maximal_latitude,
        minimal_depth,
        maximal_depth,
        vertical_dimension_as_originally_produced,
        start_datetime,
        end_datetime,
        output_filename,
        force_service,
        request_file,
        output_directory,
        credentials_file,
        motu_api_request,
        force_download,
        overwrite_output_data,
        overwrite_metadata_cache,
        no_metadata_cache,
    )
