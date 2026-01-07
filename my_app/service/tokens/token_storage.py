"""
Token storage module.

This module provides functionality for storing and managing authentication
tokens obtained from the OAuth2 authentication service.
"""

from my_app.schemas.authentication import AuthenticationResponse

_tokens = None


def store_tokens(auth_data):
    """
    Store authentication tokens from API response.

    Converts the authentication response data into an AuthenticationResponse
    object and stores it globally for use throughout the application.

    Args:
        auth_data (dict): Dictionary containing token data from the
            authentication API response. Expected keys:
            - token_type: Type of token (e.g., "Bearer")
            - expires_in: Token expiration time in seconds
            - access_token: The access token string
            - refresh_token: The refresh token string

    Returns:
        AuthenticationResponse: The stored authentication response object.
    """
    global _tokens

    _tokens = AuthenticationResponse(
        token_type=auth_data["token_type"],
        expires_in=auth_data["expires_in"],
        access_token=auth_data["access_token"],
        refresh_token=auth_data["refresh_token"],
    )
