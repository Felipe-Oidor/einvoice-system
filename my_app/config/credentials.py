"""
Credentials module for authentication.

This module creates an object by obtaining credentials from environment variables
defined in a `.env` file.

Attributes:
    authentication_credentials (Authentication): Object containing the username,
        password, client ID, and client secret required for OAuth2 authentication.
        These credentials are provided by the supplier.
"""

from os import getenv
from dotenv import load_dotenv
from my_app.schemas.authentication import Authentication

# Load environment variables from the .env file
load_dotenv()

# Create an authentication object using credentials from environment variables
authentication_credentials = Authentication(
    username=getenv("USERNAME"),
    password=getenv("PASSWORD"),
    client_id=getenv("CLIENT_ID"),
    client_secret=getenv("CLIENT_SECRET"),
)
