"""
Token Storage Module

This module stores access tokens from the authentication module.
"""

import time

# Tokens storage
_tokens = None


def tokens_store(tokens) -> None:
    """
    Save access tokens.

    Args:
        - tokens (dict): Access tokens from the authentication module.
    """
    global _tokens
    tokens["expires_in"] = time.time() + tokens["expires_in"]
    _tokens = tokens
