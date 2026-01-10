"""
Authentication service module.

This module handles the initial authentication process by obtaining
access tokens from the OAuth2 authentication endpoint.
"""

from my_app.config.constants import ENDPOINTS
from my_app.utils.http_utils import http_request
from my_app.config.credentials import authentication_credentials
from my_app.service.tokens.token_storage import store_tokens


def authenticate():
    """
    Authenticate and obtain access tokens.

    Performs OAuth2 password grant authentication using credentials
    from the environment and stores the obtained tokens internally
    via the token storage service.

    The function does not return a value; tokens are stored automatically
    and can be retrieved using the token storage service.
    """

    url_auth = ENDPOINTS.get("authentication")["login"]

    body = authentication_credentials.authentication_payload()

    header = authentication_credentials.authentication_header()

    response = http_request(
        method="POST",
        url=url_auth,
        data=body,
        headers=header,
    )

    # Check if response is an error string
    if isinstance(response, str):
        raise RuntimeError(f"Authentication failed: {response}")

    store_tokens(auth_data=response.json())
