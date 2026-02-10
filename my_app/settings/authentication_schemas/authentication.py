"""
Authentication Module

This module loads the credentials from `.env` file using SecretStr, BaseSettings, and SettingsConfigDict
from pydantic and pydantic-settings.
"""

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Authentication(BaseSettings):
    """
    Authentication Object

    This class contains credentials, authentication header, and authentication payload
    data needed to authenticate.

    Methods:
        - authentication_header(): Returns header needed for OAuth2 authentication.
        - authentication_payload(): Returns the payload needed for OAuth2 authentication.
    """

    # Credentials loaded from .env file
    username: SecretStr
    password: SecretStr
    client_id: SecretStr
    client_secret: SecretStr

    # Configuration for loading environment variables
    model_config = SettingsConfigDict(
        env_prefix="APP_",  # prefix for environment variables
        env_file=".env",  # file to load
        env_encoding="UTF-8",  # file encoding
    )

    # Authentication Header
    def authentication_header(self) -> dict:
        """
        Returns a dictionary with headers needed for authentication.
        """
        return {"Accept": "application/json"}

    # Authentication Payload
    def authentication_payload(self) -> dict:
        """
        Returns a dictionary with the payload for authentication.
        """
        return {
            "grant_type": "password",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "username": self.username.get_secret_value(),
            "password": self.password.get_secret_value(),
        }
