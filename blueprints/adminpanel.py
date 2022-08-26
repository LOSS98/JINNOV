from datetime import datetime
import shutil
import time
import os
from traceback import format_exc
from flask import Blueprint, redirect, render_template, abort, request, url_for
from models import auth_manager, utils
from models.database import sql_connector, objects

adminpanel = Blueprint("adminpanel", __name__)

# Articles


@adminpanel.route("/articles")
def articles():
    return render_template(
        "articles.html", articles=sql_connector.sql_connector.get_all_articles()
    )


@adminpanel.route("/articles/<id>", methods=["GET"])
def article(id):
    article = sql_connector.sql_connector.get_article(id)
    if article is not None:
        return render_template("article.html", article=article)
    abort(404)


@adminpanel.route("/articles/delete/<id>", methods=["GET"])
def article_delete(id):
    if auth_manager.is_connected():
        article = sql_connector.sql_connector.get_article(id)
        if article is not None:
            sql_connector.sql_connector.delete_article(article)
            shutil.rmtree("static/articles/" + article.image.split("/")[1])
            return redirect(url_for("adminpanel.articles"))
        abort(404)
    abort(401)


@adminpanel.route("/new-article", methods=["GET"])
def create_article():
    if auth_manager.is_connected():
        return render_template(
            "article_form.html",
            authors={
                membre.id: membre.first_name + " " + membre.last_name
                for membre in sql_connector.sql_connector.get_all_membres()
            },
        )
    abort(401)


@adminpanel.route("/new-article", methods=["POST"])
def create_article_post():
    if auth_manager.is_connected():
        title = request.form.get("title")
        image = request.files.get("image")
        body = request.form.get("body")
        author = request.form.get("author")
        date = request.form.get("date")
        attachements = request.files.getlist("attachements")
        if (
            title is not None
            and image is not None
            and body is not None
            and author is not None
            and date is not None
        ):
            try:
                now = int(time.time_ns())
                os.makedirs(f"static/articles/{now}", exist_ok=True)
                extension = os.path.splitext(image.filename)[1][1:].lower()
                if extension in utils.ALLOWED_EXTENSIONS:
                    image_path = f"articles/{now}/image.{extension}"
                    image.save("static/" + image_path)
                    attachements_path = []
                    for i in range(len(attachements)):
                        extension = os.path.splitext(image.filename)[1][1:].lower()
                        if extension in utils.ALLOWED_EXTENSIONS:
                            extra_path = f"articles/{now}/attachement_{i}.{extension}"
                            attachements[i].save("static/" + extra_path)
                            attachements_path.append(extra_path)
                        else:
                            abort(400)
                    date = int(
                        time.mktime(datetime.strptime(date, "%Y-%m-%d").timetuple())
                    )
                    author = int(author)
                    sql_connector.sql_connector.upsert_article(
                        objects.Article(
                            None,
                            author,
                            date,
                            title,
                            body,
                            image_path,
                            ",".join(attachements_path),
                            None,
                        )
                    )
                    return redirect(url_for("adminpanel.articles"))
            except Exception as _:
                print(format_exc())
        abort(400)
    abort(401)
