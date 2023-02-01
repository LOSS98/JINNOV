from flask import Flask, render_template
from dotenv import load_dotenv
from models.database import sql_connector
from models.utils import *
import os
import blueprints

# Fields
app = Flask(__name__)


@app.route("/formulaire_etudiant", methods=["GET", "POST"])
def etuform():
    return render_template("mail_form_student.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/qui_sommes_nous")
def aboutus():
    return render_template("kisomnou.html")


@app.route("/etudes")
def etudes():
    return render_template("soon.html")


@app.route("/liste_membres")
def liste_membres():
    return render_template("soon.html")


# Register blueprints
app.register_blueprint(blueprints.auth.auth)
app.register_blueprint(blueprints.adminpanel.adminpanel)
app.register_blueprint(blueprints.core.core)

# Load .env variables
if not os.path.exists(".env"):
    raise Exception("EnvFileNotFound")
load_dotenv()

# Dirs
os.makedirs("static/articles", exist_ok=True)
os.makedirs("static/etudes", exist_ok=True)

# Database System
sql_connector.sql_connector = sql_connector.SQLConnector(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USERNAME"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME"),
)
sql_connector.sql_connector.connect()

# Secret Key reading
if not os.path.exists("secret.key"):
    raise Exception("SecretKeyNotFound")
with open("secret.key") as key:
    app.config["SECRET_KEY"] = key.read()


if __name__ == "__main__":

    # Running
    app.run(host="0.0.0.0", port=80, debug=False)
