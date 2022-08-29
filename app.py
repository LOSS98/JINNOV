from flask import Flask, render_template
from models.database import sql_connector

import os
import blueprints

# Fields
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # Dirs
    os.makedirs("static/articles", exist_ok=True)
    os.makedirs("static/etudes", exist_ok=True)

    # Database System
    sql_connector.sql_connector = sql_connector.SQLConnector(
        host="127.0.0.1", user="root", password="", database="jinnov"
    )
    sql_connector.sql_connector.connect()

    # Secret Key reading
    if not os.path.exists("secret.key"):
        raise Exception("SecretKeyNotFound")
    with open("secret.key") as key:
        app.config["SECRET_KEY"] = key.read()

    # Register blueprints
    app.register_blueprint(blueprints.auth.auth)
    app.register_blueprint(blueprints.adminpanel.adminpanel)
    app.register_blueprint(blueprints.core.core)

    # Running
    app.run(host="0.0.0.0", port=80, debug=False)
