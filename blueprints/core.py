from flask import Blueprint, render_template, abort
from models import auth_manager, utils
from models.database import sql_connector

core = Blueprint("core", __name__)


@core.route("/articles")
def articles():
    return render_template(
        "articles.html", articles=sql_connector.sql_connector.get_all_articles()
    )


@core.route("/articles/<id>", methods=["GET"])
def article(id):
    article = sql_connector.sql_connector.get_article(id)
    if article is not None:
        return render_template(
            "article.html", article=article, admin=auth_manager.is_connected())
        
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
            "etude.html", etude=etude, admin=auth_manager.is_connected())
    abort(404)


@core.route("/ask-devis", methods=["POST"])
def post_devis():
    return render_template("soon.html")
    # return utils.create_mail_devis()
    
@core.route('/mail_student', methods=["POST"])
def post_student():
    # return utils.create_mail_student()
    return render_template("soon.html")
