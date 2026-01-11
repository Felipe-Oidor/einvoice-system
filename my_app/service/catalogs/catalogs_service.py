"""
Catalogs service module.

This module retrieves catalogs needed for issuing electronic invoices,
including numbering ranges, municipalities, tributes, and unit measurements.
"""

from my_app.service.tokens.token_storage import _tokens
from my_app.schemas.catalogs import CatalogsHeader
from my_app.utils.http_utils import http_request
from my_app.config.constants import ENDPOINTS


def get_catalogs(catalog):
    """
    Retrieve catalog data from the API.

    Makes a GET request to fetch a specific catalog required for electronic
    invoice processing. The available catalogs are:
    - numberingRange: Numbering ranges for invoice documents
    - municipalities: Municipal information
    - tributes: Tax and tribute information
    - unitMeasurement: Unit of measurement standards

    Args:
        catalog (str): The name of the catalog to retrieve. Must be one of:
            "numberingRange", "municipalities", "tributes", or "unitMeasurement".

    Returns:
        dict: A dictionary containing the catalog data in JSON format.
            The structure depends on the requested catalog type.
    """
    url_catalogs = ENDPOINTS.get("catalogs")[catalog]

    header = CatalogsHeader.header(token=_tokens.access_token.get_secret_value())

    response = http_request(method="GET", url=url_catalogs, headers=header)

    # Check if response is an error string
    if isinstance(response, str):
        raise RuntimeError(f"Failed to retrieve catalog '{catalog}': {response}")

    return response.json()
