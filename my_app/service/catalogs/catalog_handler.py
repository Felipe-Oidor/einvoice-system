"""
Catalog handler module.

This module provides functions for processing and extracting data from
stored catalog structures.
"""

from my_app.service.catalogs.catalogs_storage import _catalogs


def extract_catalog_data(catalog):
    """
    Extract catalog data from stored catalog structure.

    Retrieves a catalog from storage and unwraps nested "data" fields
    to return the actual catalog data. The function handles cases where
    the data may be nested within multiple levels of "data" keys.

    Args:
        catalog (str): The name of the catalog to extract. Must be one of:
            "numberingRange", "municipalities", "tributes", or "unitMeasurement".

    Returns:
        dict: The unwrapped catalog data with all nested "data" layers removed.

    """
    data = _catalogs.get(catalog)["data"]

    while isinstance(data, dict) and "data" in data:
        data = data["data"]

    return data