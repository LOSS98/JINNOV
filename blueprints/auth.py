from flask import Blueprint, flash, redirect, render_template, url_for, request
from models import auth_manager

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    if auth_manager.login(email=email, password=password):
        return redirect(url_for("index"))
    else:
        flash("Identifiants incorrects !")
        return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    auth_manager.logout()
    return redirect(url_for("index"))


@auth.route("/profile")
def profile():
    user = auth_manager.get_current_user()
    return render_template(
        "profile.html", name=user.full_name if user is not None else None
    )
