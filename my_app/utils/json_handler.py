"""
JSON file handler utility module.

This module provides functions for reading and parsing JSON files.
"""

import json


def load_json(file_path: str, file_mode: str = "r", extract_key: str = None) -> dict:
    """
    Load and parse a JSON file.

    Reads a JSON file and optionally extracts a specific key from the
    parsed data.

    Args:
        file_path (str): Path to the JSON file to load.
        file_mode (str, optional): File opening mode. Defaults to "r".
        extract_key (str, optional): If provided, returns the value associated
            with this key from the JSON data. If None, returns the
            entire parsed JSON object.

    Returns:
        dict: The parsed JSON data, or a subset if 'extract_key' parameter
            is specified.
    """
    with open(file_path, file_mode) as file:
        # data = json.load(file)
        if not extract_key:
            return json.load(file)
        return json.load(file).get(extract_key)
