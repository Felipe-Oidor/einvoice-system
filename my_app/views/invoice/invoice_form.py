from flask import Blueprint, render_template

bp = Blueprint("invoice_form", __name__, url_prefix="/crear-factura")


@bp.route("/")
def hello_world():
    return render_template("invoice_form/base-form.html")
