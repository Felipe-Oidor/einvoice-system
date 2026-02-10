"""
Refresh Token Module

This module handles refreshing the authentication tokens.
"""

from my_app.settings.constants import ENDPOINTS
from my_app.utils.http_utils import http_requests
from my_app.settings.authentication_schemas.refresh_token import RefreshToken
from my_app.services.tokens.tokens_storage import _tokens, tokens_store


def refresh_token():
    """
    Refreshes the authentication tokens.
    """
    endpoint = ENDPOINTS["authentication"]["refresh_token"]
    credentials = RefreshToken()
    header = credentials.refresh_header()
    payload = credentials.refresh_payload(refresh_token=_tokens["refresh_token"])

    response = http_requests(method="POST", url=endpoint, data=payload, headers=header)

    tokens_store(tokens=response)
