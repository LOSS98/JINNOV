from crypt import methods
from flask import Blueprint, redirect, render_template, url_for, request

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    return redirect(url_for("index"))


@auth.route("/logout")
def logout():
    return "Logout"
