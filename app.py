from flask import Flask, render_template
from flask_login import LoginManager
from models.database import sql_connector

import os

# Fields
app = Flask(__name__)
login_manager = LoginManager()


# Admin Login System
@login_manager.user_loader
def load_user(user_id: str):
    return None


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "main":

    # Database System
    sql_connector.sql_connector = sql_connector.SQLConnector()

    # Login System
    login_manager.init_app(app)

    # Secret Key reading
    if not os.path.exists("secret.key"):
        raise Exception("SecretKeyNotFound")
    with open("secret.key") as key:
        app.config["SECRET_KEY"] = key.read()

    # Running
    app.run(host="0.0.0.0", port=80, debug=False)
