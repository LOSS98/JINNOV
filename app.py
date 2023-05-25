from flask import Flask, render_template
from dotenv import load_dotenv
from models.database import sql_connector
from models.utils import *
import os
import blueprints

# Fields
app = Flask(__name__)

def getAgreement():
    agreement = request.cookies.get("agreement")
    return ['true','false'][agreement==None],agreement

@app.route("/formulaire_etudiant", methods=["GET", "POST"])
def etuform():
    has,agr = getAgreement()
    return render_template("mail_form_student.html",has_agreed=has,agreement=agr)


@app.route("/")
def index():
    has,agr = getAgreement()
    return render_template("index.html",has_agreed=has,agreement=agr)


@app.route("/contact")
def contact():
    has,agr = getAgreement()
    return render_template("contact.html",has_agreed=has,agreement=agr)


@app.route("/qui_sommes_nous")
def aboutus():
    has,agr = getAgreement()
    return render_template("kisomnou.html",has_agreed=has,agreement=agr)


@app.route("/etudes")
def etudes():
    has,agr = getAgreement()
    return render_template("soon.html",has_agreed=has,agreement=agr)


@app.route("/liste_membres")
def liste_membres():
    has,agr = getAgreement()
    return render_template("soon.html",has_agreed=has,agreement=agr)

@app.route('/prestations')
def presta():
    has,agr = getAgreement()
    return render_template("presta.html",has_agreed=has,agreement=agr)

@app.route('/prestations/developpement_web')
def devweb():
    has,agr = getAgreement()
    return render_template("prestations/devweb.html",has_agreed=has,agreement=agr)

@app.route('/prestations/developpement_mobile')
def devmobile():
    has,agr = getAgreement()
    return render_template("prestations/devmobile.html",has_agreed=has,agreement=agr)

@app.route('/prestations/audit_informatique')
def auditinfo():
    has,agr = getAgreement()
    return render_template("prestations/auditinfo.html",has_agreed=has,agreement=agr)

@app.route('/prestations/protections_des_donnees')
def protectiondonnees():
    has,agr = getAgreement()
    return render_template("prestations/protectiondonnees.html",has_agreed=has,agreement=agr)

@app.route('/prestations/audit_energetique')
def auditenergetique():
    has,agr = getAgreement()
    return render_template("prestations/auditenergetique.html",has_agreed=has,agreement=agr)

@app.route('/prestations/dimensionnement')
def dimensionnement():
    has,agr = getAgreement()
    return render_template("prestations/dimensionnement.html",has_agreed=has,agreement=agr)

@app.route('/prestations/modelisation')
def modelisation():
    has,agr = getAgreement()
    return render_template("prestations/modelisation.html",has_agreed=has,agreement=agr)

@app.route('/prestations/prototypage')
def prototypage():
    has,agr = getAgreement()
    return render_template("prestations/prototypage.html",has_agreed=has,agreement=agr)


@app.errorhandler(404)
def knowhere(it):
    has,agr = getAgreement()
    return render_template("404.html",has_agreed=has,agreement=agr)

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
