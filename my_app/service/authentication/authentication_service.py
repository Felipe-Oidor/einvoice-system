"""
Authentication service module.

This module handles the initial authentication process by obtaining
access tokens from the OAuth2 authentication endpoint.
"""

from my_app.config.constants import ENDPOINTS
from my_app.utils.http_request import post_request
from my_app.config.credentials import authentication_credentials
from my_app.service.tokens.token_storage import store_tokens


def authenticate():
    """
    Authenticate and obtain access tokens.

    Performs OAuth2 password grant authentication using credentials
    from the environment and stores the obtained tokens.

    Returns:
        AuthenticationResponse: The authentication response containing
            access token, refresh token, and expiration information.
    """
    response = post_request(
        url=ENDPOINTS.get("authentication")["auth"],
        data=authentication_credentials.authentication_payload(),
        headers=authentication_credentials.authentication_header(),
    )

    store_tokens(auth_data=response.json())
