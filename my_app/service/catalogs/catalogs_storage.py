"""
Store catalog module.

This module stores catalog data required for invoice generation, such as
numbering ranges, municipalities, tributes, and units of measurement.

Attributes:
    _catalogs: Internal storage for all retrieved catalog data.
"""

from my_app.service.catalogs.catalogs_service import get_catalogs
from my_app.config.constants import ENDPOINTS


_catalogs = None


def store_catalogs():
    global _catalogs

    if _catalogs is None:
        catalog_name = ENDPOINTS.get("catalogs").keys()

        _catalogs = {name: get_catalogs(catalog=name) for name in catalog_name}
