"""
Refresh token service module.

This module handles the renewal of access tokens using refresh tokens
obtained from the initial authentication process.
"""

from my_app.config.constants import ENDPOINTS
from my_app.utils.http_utils import http_request
from my_app.config.credentials import authentication_credentials
from my_app.service.tokens.token_storage import _tokens, store_tokens


def refresh_access_token():
    """
    Refresh the access token using a stored refresh token.

    Retrieves the stored refresh token and uses it to obtain a new
    access token from the authentication endpoint. The new tokens
    are stored internally via the token storage service.

    The function does not return a value; tokens are stored automatically
    and can be retrieved using the token storage service.
    """
    url_refresh = ENDPOINTS.get("authentication")["refreshToken"]

    body = authentication_credentials.refresh_payload(
        refresh_token=_tokens.refresh_token.get_secret_value()
    )

    header = authentication_credentials.refresh_header(
        _tokens.access_token.get_secret_value()
    )

    response = http_request(
        method="POST",
        url=url_refresh,
        data=body,
        headers=header,
    )

    # Check if response is an error string
    if isinstance(response, str):
        raise RuntimeError(f"Token refresh failed: {response}")

    store_tokens(auth_data=response.json())
