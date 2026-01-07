"""
Constants module for API configuration.

This module loads and exposes configuration data used throughout the application.

Attributes:
    ENDPOINTS (dict): Dictionary containing the URLs for the API endpoints.
    DOCUMENT_TYPE (dict): Dictionary containing the codes for the different document types.
"""

from my_app.utils.json_handler import load_json

# Load API endpoints
ENDPOINTS = load_json(file_path="my_app/data/endpoints.json")

# Load document type codes
DOCUMENT_TYPE = load_json(file_path="my_app/data/document_type_code.json")
