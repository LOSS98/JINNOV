from flask import Flask, render_template
from models.database import sql_connector
from models.utils import *
import os
import blueprints

# Fields
app = Flask(__name__)

@app.route('/formulaire_etudiant', methods=["GET","POST"])
def etuform():
    return render_template("mail_form_student.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/qui_sommes_nous')
def aboutus():
    return render_template("kisomnou.html")

@app.route('/actualites')
def actualites():
    return render_template("soon.html")

@app.route('/etudes')
def etudes():
    return render_template("soon.html")

@app.route('/liste_membres')
def liste_membres():
    return render_template("soon.html")

@app.route('/prestations')
def presta():
    return render_template("presta.html")

if __name__ == "__main__":
    # Running
    app.run(host="0.0.0.0", port=80, debug=True)
