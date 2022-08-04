from datetime import datetime
import time
from flask import Blueprint, redirect, render_template, abort, request, url_for
from models import auth_manager
from models.database import sql_connector, objects

adminpanel = Blueprint("adminpanel", __name__)

# Articles


@adminpanel.route("/etudes")
def etudes():
    return render_template(
        "etudes.html", etudes=sql_connector.sql_connector.get_all_etudes()
    )


@adminpanel.route("/etudes/<id>", methods=["GET"])
def etude(id):
    etude = sql_connector.sql_connector.get_etude(id)
    if etude is not None:
        return render_template("etude.html", etude=etude)
    abort(404)


@adminpanel.route("/etudes/delete/<id>", methods=["GET"])
def etude_delete(id):
    if auth_manager.is_connected():
        etude = sql_connector.sql_connector.get_etude(id)
        if etude is not None:
            sql_connector.sql_connector.delete_etude(etude)
            return redirect(url_for("adminpanel.etudes"))
        abort(404)
    abort(401)


@adminpanel.route("/new-etude", methods=["GET"])
def create_etude():
    if auth_manager.is_connected():
        return render_template("etude_form.html")
    abort(401)


@adminpanel.route("/new-etude", methods=["POST"])
def create_etude_post():
    if auth_manager.is_connected():
        customer_name = request.form.get("customer_name")
        body = request.form.get("body")
        customer_link = request.form.get("customer_link")
        date = request.form.get("date")
        if (
            customer_name is not None
            and body is not None
            and customer_link is not None
            and date is not None
        ):
            try:
                date = int(time.mktime(datetime.strptime(date, "%Y-%m-%d").timetuple()))
                sql_connector.sql_connector.upsert_etude(
                    objects.Etude(None, date, customer_name, customer_link, body)
                )
                return redirect(url_for("adminpanel.etudes"))
            except ValueError as _:
                pass
        abort(400)
    abort(401)
