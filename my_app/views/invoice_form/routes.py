"""
Blueprints and routes for the invoice form.

This module defines the routes related to the electronic invoice form
using a Flask Blueprint.
"""

from flask import Blueprint

form_bp = Blueprint("form", __name__, url_prefix="/form")
"""
Blueprint for invoice form routes.

This Blueprint groups all routes related to the invoice form.
All routes defined in this Blueprint have the '/form' prefix
in their URL.

Attributes:
    name (str): Name of the blueprint ('form').
    url_prefix (str): URL prefix for all routes ('/form').
"""

@form_bp.route("/")
def form():
    return "<h1>Form</h1>"