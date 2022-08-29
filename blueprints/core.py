from flask import Blueprint, render_template, abort
from models import auth_manager
from models.database import sql_connector

core = Blueprint("core", __name__)


@core.route("/etudes")
def etudes():
    return render_template(
        "etudes.html", etudes=sql_connector.sql_connector.get_all_etudes()
    )


@core.route("/etudes/<id>", methods=["GET"])
def etude(id):
    etude = sql_connector.sql_connector.get_etude(id)
    if etude is not None:
        return render_template(
            "etude.html", etude=etude, admin=auth_manager.is_connected()
        )
    abort(404)
