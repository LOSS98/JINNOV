from email import message
import smtplib, ssl
from flask import Flask, render_template, request, redirect, send_file, url_for, flash, jsonify
import MySQLdb as mysql

def send_mail(nom_entreprise:str,nom:str,prenom:str,adresse:str,telephone:str,contenu:str,mail:str):
    """Procedure envoyant un e-mail vers une boite mail dédié"""

    port = 465 
    smtp_server = "smtp.gmail.com"
    sender_email = "devis@jinnov-insa.fr"  # Enter your address
    receiver_email = "jn.bonvent@gmail.com"  # Enter receiver address
    password = "ueieyfvwqizjrmrv" #mdp d'application généré depuis google

    message = """From: <jn.bonvent@gmail.com>
To: <jn.bonvent@gmail.com>
Subject: %s
MIME-Version : 1.0
Encoding : UTF-8
Nom de l'entreprise = %s
Nom et prenom du contact = %s %s
Adresse de l'entreprise = %s
Mail de contact = % s
Téléphone = %s
Demande =  \n%s
""" % ('demande de devis ' + str(nom_entreprise), nom_entreprise, nom,prenom,adresse,mail,telephone,contenu)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

send_mail('GOOGLE','Doe',"John","15 rue lafarge","téléphone","un long text é ddddd",'mail@gnail.com')


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    return render_template("mail_form.html")

@app.route('/mail', methods=["GET","POST"])
def mail():
    if request.method == 'POST':
        nom_entreprise:str = request.form.get('nom_entreprise')
        nom:str = request.form.get('nom')
        prenom:str = request.form.get('prenom')
        adresse:str = request.form.get('Adresse')
        telephone:str = request.form.get('téléphone')
        contenu:str =request.form.get('contenu')
        mail:str =request.form.get('mail')
        send_mail(nom_entreprise,nom,prenom,adresse,telephone,contenu,mail)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)