from flask import Flask


def create_app():

    app = Flask(__name__)

    from my_app.views.invoice.invoice_form import bp

    app.register_blueprint(bp)

    return app
