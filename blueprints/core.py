from flask import Blueprint, render_template, abort,request
from models import auth_manager, utils
from models.database import sql_connector

core = Blueprint("core", __name__)

def getAgreement():
    agreement = request.cookies.get("agreement")
    return ['true','false'][agreement==None],agreement

@core.route("/actualites")
def articles():
    has,agr = getAgreement()
    liste = sql_connector.sql_connector.get_all_articles()
    highlighted = None
    if len(liste) > 0:
        liste.sort(key=lambda a: a.created_at, reverse=True)
        highlighted = liste.pop(0)
    return render_template("articles.html", articles=liste, highlighted=highlighted,has_agreed=has,agreement=agr)


@core.route("/actualites/<id>", methods=["GET"])
def article(id):
    has,agr = getAgreement()
    article = sql_connector.sql_connector.get_article(id)
    if article is not None:
        return render_template(
            "article.html", article=article, admin=auth_manager.is_connected(),
            has_agreed=has,agreement=agr
        )
    abort(404)


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


@core.route("/ask-devis", methods=["POST"])
def post_devis():
    return utils.create_mail_devis()


@core.route("/mail_student", methods=["POST"])
def post_student():
    return utils.create_mail_student()
