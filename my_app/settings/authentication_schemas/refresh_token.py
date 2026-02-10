"""
Refresh Token Schema Module

This module defines the data needed to send a refresh token request.
"""

from my_app.settings.authentication_schemas.authentication import Authentication


class RefreshToken(Authentication):
    """
    Refresh Token Class

    This class contains the header and payload data needed to refresh
    the access token.

    Methods:
        - refresh_header(): Returns header needed for refresh token.
        - refresh_payload(): Returns the payload needed for refresh token.
    """

    @staticmethod
    def refresh_header():
        return {"Authorization": "", "Accept": "application/json"}

    def refresh_payload(self, refresh_token):
        return {
            "grant_type": "refresh_token",
            "client_id": self.client_id.get_secret_value(),
            "client_secret": self.client_secret.get_secret_value(),
            "refresh_token": refresh_token,
        }
