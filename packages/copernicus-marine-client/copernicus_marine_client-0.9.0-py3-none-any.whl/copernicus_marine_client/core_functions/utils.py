import pathlib
from typing import Callable, Iterable, Iterator, Optional, TypeVar

OVERWRITE_SHORT_OPTION = "--overwrite"
OVERWRITE_LONG_OPTION = "--overwrite-output-data"
OVERWRITE_OPTION_HELP_TEXT = (
    "If specified and if the file already exists on destination, then it will be "
    "overwritten instead of creating new one with unique index."
)

FORCE_DOWNLOAD_CLI_PROMPT_MESSAGE = "Do you want to proceed with download?"

DEFAULT_CLIENT_BASE_DIRECTORY = (
    pathlib.Path.home() / ".copernicus-marine-client"
)


def get_unique_filename(
    filepath: pathlib.Path, overwrite_option: bool
) -> pathlib.Path:
    if not overwrite_option:
        parent = filepath.parent
        filename = filepath.stem
        extension = filepath.suffix
        counter = 1

        while filepath.exists():
            filepath = parent / (
                filename + "_(" + str(counter) + ")" + extension
            )
            counter += 1

    return filepath


_T = TypeVar("_T")
_S = TypeVar("_S")


def map_reject_none(
    function: Callable[[_S], Optional[_T]], iterable: Iterable[_S]
) -> Iterable[_T]:

    return (element for element in map(function, iterable) if element)


def next_or_raise_exception(
    iterator: Iterator[_T], exception_to_raise: Exception
) -> _T:
    try:
        return next(iterator)
    except Exception as exception:
        raise exception_to_raise from exception


def flatten(list: list[list[_T]]) -> list[_T]:
    return [item for sublist in list for item in sublist]
