"""
Constants Module.

This module contains the constants used by the application.
"""

from my_app.utils.json_handler import json_load

# Load endpoints
ENDPOINTS = json_load(json_file="my_app/data/endpoints.json")
