"""
Authentication schemas for OAuth2-based token handling.

This module defines Pydantic models used to:
- Build authentication and refresh payloads
- Safely handle sensitive credentials and tokens using SecretStr
"""

from pydantic import BaseModel, SecretStr


class Authentication(BaseModel):
    """
    Holds user credentials and builds OAuth authentication payloads.

    This model encapsulates sensitive values using SecretStr and exposes
    helper methods to generate payloads for:
    - password grant authentication
    - refresh token flow
    """

    username: SecretStr
    password: SecretStr
    client_id: SecretStr
    client_secret: SecretStr

    def authentication_header(self) -> dict:
        """
        Build HTTP headers for OAuth2 password grant authentication request.

        Returns:
            dict: HTTP headers dictionary containing the Accept header
                set to "application/json" for the authentication request.
        """
        return {"Accept": "application/json"}

    def authentication_payload(self) -> dict:
        """
        Build an OAuth2 password grant Payload.

        Returns:
            dict: Payload suitable for an OAuth2 token endpoint using the
            `password` grant type.
        """
        return {
            "grant_type": "password",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "username": self.username.get_secret_value(),
            "password": self.password.get_secret_value(),
        }

    def refresh_header(self, token) -> dict:
        """
        Build HTTP headers for OAuth2 refresh token request.

        Args:
            token (str): Access token to include in the Authorization header
                as a Bearer token.

        Returns:
            dict: HTTP headers dictionary containing:
                - Authorization header with Bearer token
                - Accept header set to "application/json"
        """
        return {"Authorization": f"Bearer {token}", "Accept": "application/json"}

    def refresh_payload(self, refresh_token: str) -> dict:
        """
        Build an OAuth2 refresh token payload.

        Args:
            refresh_token (str): Previously issued refresh token.

        Returns:
            dict: Payload suitable for refreshing an access token.
        """
        return {
            "grant_type": "refresh_token",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "refresh_token": refresh_token,
        }


class AuthenticationResponse(BaseModel):
    """
    Represents the token response returned by an authentication endpoint.
    """

    token_type: SecretStr
    expires_in: int
    access_token: SecretStr
    refresh_token: SecretStr

    def data_response(self) -> dict:
        """
        Returns the token data obtained from the API response.
        """
        return {
            "token_type": self.token_type.get_secret_value(),
            "expires_in": self.expires_in,
            "access_token": self.access_token.get_secret_value(),
            "refresh_token": self.refresh_token.get_secret_value(),
        }
