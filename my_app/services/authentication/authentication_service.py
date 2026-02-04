"""
Authentication Module.

This module handles the authentication process and stores access tokens.
"""

from my_app.settings.constants import ENDPOINTS
from my_app.utils.http_utils import http_requests
from my_app.settings.authentication import Authentication
from my_app.services.tokens.tokens_storage import tokens_store


def authentication() -> None:
    """
    Sends a POST request to obtain access tokens and save them for reuse.
    """
    endpoint = ENDPOINTS["authentication"]["authentication_url"]
    credentials = Authentication()
    payload = credentials.authentication_payload()
    header = credentials.authentication_header()

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    tokens_store(tokens=response)
