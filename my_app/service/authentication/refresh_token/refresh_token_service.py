"""
Refresh token service module.

This module handles the renewal of access tokens using refresh tokens
obtained from the initial authentication process.
"""

from my_app.config.constants import ENDPOINTS
from my_app.utils.http_request import post_request
from my_app.config.credentials import authentication_credentials
from my_app.service.tokens.token_storage import _tokens, store_tokens


def refresh_access_token():
    """
    Refresh the access token using a stored refresh token.

    Retrieves the stored refresh token and uses it to obtain a new
    access token from the authentication endpoint.

    Returns:
        AuthenticationResponse: The refreshed authentication response
            containing new access token, refresh token, and expiration
            information.
    """
    response = post_request(
        url=ENDPOINTS.get("authentication")["refresh"],
        data=authentication_credentials.refresh_payload(
            refresh_token=_tokens.refresh_token.get_secret_value()
        ),
        headers=authentication_credentials.refresh_header(
            _tokens.access_token.get_secret_value()
        ),
    )

    store_tokens(auth_data=response.json())
