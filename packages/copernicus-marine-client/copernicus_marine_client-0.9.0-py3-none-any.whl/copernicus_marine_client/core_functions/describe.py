import json

from copernicus_marine_client.catalogue_parser.catalogue_parser import (
    CopernicusMarineCatalogue,
    filter_catalogue_with_strings,
    parse_catalogue,
)


def describe_function(
    include_description: bool,
    include_datasets: bool,
    include_keywords: bool,
    contains: list[str],
    overwrite_metadata_cache: bool,
    no_metadata_cache: bool,
) -> str:
    base_catalogue: CopernicusMarineCatalogue = parse_catalogue(
        overwrite_metadata_cache=overwrite_metadata_cache,
        no_metadata_cache=no_metadata_cache,
    )

    catalogue_dict = (
        filter_catalogue_with_strings(base_catalogue, contains)
        if contains
        else base_catalogue.__dict__
    )

    def default_filter(obj):
        attributes = obj.__dict__
        attributes.pop("_name_", None)
        attributes.pop("_value_", None)
        attributes.pop("__objclass__", None)
        if not include_description:
            attributes.pop("description", None)
        if not include_datasets:
            attributes.pop("datasets", None)
        if not include_keywords:
            attributes.pop("keywords", None)
        return obj.__dict__

    json_dump = json.dumps(
        catalogue_dict, default=default_filter, sort_keys=False, indent=2
    )
    return json_dump
