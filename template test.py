from flask import Flask, render_template
from models.utils import *

# Fields

app = Flask(__name__)

@app.route('/formulaire_etudiant', methods=["GET","POST"])
def etuform():
    return render_template("mail_form_student.html")

#route pour la création de devis
@app.route('/mail_devis', methods=["POST"])
def mail_devis():
    return create_mail_devis()
    
#route pour la création d"une demande d'inscriptions
@app.route('/mail_student', methods=["POST"])
def mail_student():
    return create_mail_student()

@app.route('/qui_sommes_nous')
def aboutus():
    return render_template("kisomnou.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    # Running
    app.run(host="0.0.0.0", port=80, debug=True)
