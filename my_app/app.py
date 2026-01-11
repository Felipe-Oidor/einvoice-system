"""
Main Flask application for the electronic invoice system.

This module initializes the Flask application and registers the blueprints
necessary for the system operation.
"""

from my_app.views.invoice_form.routes import form_bp
from flask import Flask

app = Flask(__name__)
"""
Main Flask application instance.

This instance is the central object of the application and is used
to register blueprints and define top-level routes.
"""

app.register_blueprint(form_bp)

@app.route("/")
def index():
    return "<h1>Flask application</h1>"