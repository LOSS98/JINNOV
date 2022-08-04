from flask import Flask, render_template
from models.database import sql_connector

import os
import blueprints

# Fields
app = Flask(__name__)

@app.route('/formulaire_etudiant', methods=["GET","POST"])
def etuform():
    return render_template("mail_form_student.html")

@app.route('/formulaire_devis', methods=["GET","POST"])
def devisform():
    return render_template("mail_form_devis.html")

#route pour la création de devis
@app.route('/mail_devis', methods=["POST"])
def mail_devis():
    return Mail_devis_create()
    
#route pour la création d"une demande d'inscriptions
@app.route('/mail_student', methods=["POST"])
def mail_student():
    return Mail_student_create()

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
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

    # Running
    app.run(host="0.0.0.0", port=80, debug=False)
