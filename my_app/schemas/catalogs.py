"""
Catalogs schemas for HTTP header generation.

This module defines schemas used to build HTTP headers for catalog API requests.
"""


class CatalogsHeader:
    """
    Provides HTTP headers for catalog API requests.

    This class contains static methods to generate the required HTTP headers
    for making requests to the catalog endpoints in the electronic invoice system.
    """

    @staticmethod
    def header(token):
        """
        Build HTTP headers for catalog API requests.

        Creates a dictionary containing the standard headers needed for
        catalog API requests, including authentication and content type headers.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
        }
