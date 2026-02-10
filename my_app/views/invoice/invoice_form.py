from flask import Blueprint

bp = Blueprint("invoice_form", __name__, url_prefix="/crear-factura")


@bp.route("/")
def hello_world():
    return "<h1>Crear Factura</h1>"
