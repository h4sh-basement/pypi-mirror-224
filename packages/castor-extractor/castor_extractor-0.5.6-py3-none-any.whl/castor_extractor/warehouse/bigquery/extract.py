import json
import logging
from collections import OrderedDict
from typing import cast

from ...logger import add_logging_file_handler
from ...utils import LocalStorage, SafeMode, from_env, write_summary
from ..abstract import (
    CATALOG_ASSETS,
    QUERIES_ASSETS,
    VIEWS_ASSETS,
    ExtractionProcessor,
    SupportedAssets,
    WarehouseAsset,
    WarehouseAssetGroup,
    common_args,
)
from .client import BigQueryClient
from .query import BigQueryQueryBuilder

logger = logging.getLogger(__name__)


BIGQUERY_CREDENTIALS = "GOOGLE_APPLICATION_CREDENTIALS"


BIGQUERY_ASSETS: SupportedAssets = OrderedDict(
    {
        WarehouseAssetGroup.CATALOG: CATALOG_ASSETS,
        WarehouseAssetGroup.QUERY: QUERIES_ASSETS,
        WarehouseAssetGroup.VIEW_DDL: VIEWS_ASSETS,
        WarehouseAssetGroup.ROLE: (WarehouseAsset.USER,),
    },
)


def _credentials(params: dict) -> dict:
    """extract GCP credentials"""
    path = params.get("credentials") or from_env(BIGQUERY_CREDENTIALS)
    logger.info(f"Credentials fetched from {path}")
    with open(path, "r") as file:
        return cast(dict, json.load(file))


def extract_all(**kwargs) -> None:
    """
    Extract all assets from BigQuery and store the results in CSV files
    Time filter scope for `Queries` = the day before (0 > 23h)
    """
    output_directory, skip_existing = common_args(kwargs)
    is_safe_mode = kwargs.get("safe_mode") or False

    safe_mode_params = None

    if is_safe_mode:
        add_logging_file_handler(output_directory)
        safe_mode_params = SafeMode((Exception,), float("inf"))

    client = BigQueryClient(
        credentials=_credentials(kwargs),
        db_allowed=kwargs.get("db_allowed"),
        db_blocked=kwargs.get("db_blocked"),
        dataset_blocked=kwargs.get("dataset_blocked"),
    )

    logger.info(f"Available projects: {client.get_projects()}\n")

    query_builder = BigQueryQueryBuilder(
        regions=client.get_regions(),
        datasets=client.get_datasets(),
    )

    storage = LocalStorage(directory=output_directory)

    extractor = ExtractionProcessor(
        client=client,
        query_builder=query_builder,
        storage=storage,
        safe_mode=safe_mode_params,
    )
    asset_count: int = 0
    for group in BIGQUERY_ASSETS.values():
        for asset in group:
            logger.info(f"Extracting `{asset.value.upper()}` ...")
            location = extractor.extract(asset, skip_existing)
            logger.info(f"Results stored to {location}\n")
            asset_count += 1

    logger.info(f"Extracted {asset_count} assets")
    if safe_mode_params:
        logger.info(f"{len(safe_mode_params.errors_caught)} assets skipped")

    write_summary(
        output_directory,
        storage.stored_at_ts,
        client_name=client.name(),
    )
