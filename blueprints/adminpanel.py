from datetime import datetime
import time
import os
from traceback import format_exc
from flask import Blueprint, redirect, render_template, abort, request, url_for
from models import auth_manager, utils
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
        return render_template(
            "etude_form.html",
            authors={
                membre.id: membre.first_name + " " + membre.last_name
                for membre in sql_connector.sql_connector.get_all_membres()
            },
        )
    abort(401)


@adminpanel.route("/new-etude", methods=["POST"])
def create_etude_post():
    if auth_manager.is_connected():
        customer_name = request.form.get("customer_name")
        image = request.files.get("icon")
        body = request.form.get("body")
        customer_link = request.form.get("customer_link")
        author = request.form.get("author")
        date = request.form.get("date")
        # TODO attachements
        if (
            customer_name is not None
            and image is not None
            and body is not None
            and customer_link is not None
            and author is not None
            and date is not None
        ):
            try:
                extension = os.path.splitext(image.filename)[1][1:].lower()
                if extension in utils.ALLOWED_EXTENSIONS:
                    image_path = f"etudes/image_{time.time_ns()}.{extension}"
                    image.save("static/" + image_path)

                    date = int(
                        time.mktime(datetime.strptime(date, "%Y-%m-%d").timetuple())
                    )
                    sql_connector.sql_connector.upsert_etude(
                        objects.Etude(
                            None,
                            date,
                            author,
                            customer_name,
                            customer_link,
                            body,
                            image_path,
                            None,
                            None,
                        )
                    )
                    return redirect(url_for("adminpanel.etudes"))
            except ValueError as _:
                pass
        abort(400)
    abort(401)
