"""
JSON Handler Module

This module handles `.json` files needed for the application
"""

import json


def json_load(json_file: str, encoding: str = "UTF-8") -> dict:
    """
    Read a JSON file and return its contents as a dictionary

    Args:
        - json_file (str): Path to the JSON file.
        - encoding: File encoding (Default: "UTF-8").

    Returns:
        - dict: Parsed JSON content.
    """
    with open(json_file, "r", encoding=encoding) as file:
        data = json.load(file)

        return data
