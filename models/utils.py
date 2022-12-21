import smtplib
import ssl
from flask import request, redirect
from email.message import EmailMessage


ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg", "gif", "jfif", "pjpeg", "jpeg", "pjp"]


def send_mail(
    message: str, sender_email: str, receiver_email: str, connection_token: str
):
    """
    This function sends an email to the receiver_email address with the message.

    :param message: The message to be sent
    :param sender_email: The email address of the sender
    :param receiver_email: The email address of the person you want to send the email to
    :param connection_token: This is the application token of the email address you're sending from
    """
    
    port = 465
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, connection_token)
        server.sendmail(sender_email, receiver_email, message)


def create_mail_devis():
    """
    It takes the data from the form, creates a message with it, and sends it to the designated mail address
    :return: the redirect function.
    """

    # fetching data
    if request.method == "POST":
        # fetching data
        nom_entreprise: str = request.form.get("nom_entreprise")
        nom: str = request.form.get("nom")
        prenom: str = request.form.get("prenom")
        adresse: str = request.form.get("Adresse")
        telephone: str = request.form.get("téléphone")
        contenu: str = request.form.get("contenu")
        mail: str = request.form.get("mail")

        # message creation
        message = f"""
            Nom de l'entreprise = {nom_entreprise}
            Nom et prenom du contact = {nom} {prenom}
            Adresse de l'entreprise (optionnel) = {adresse}
            Mail de contact = {mail}
            Téléphone = {telephone}
            Demande =  \n{contenu}
            """

        # mail connection informations
        sender_email = ""
        receiver_email = ""
        connection_token = ""

        # mail creation
        msg = EmailMessage()
        msg["MIME-Version"] = "1.0"
        msg["Subject"] = str("demande de devis " + nom_entreprise)
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(message)

        message = str(msg)

        send_mail(message, sender_email, receiver_email, connection_token)
        return redirect("/")


def create_mail_student():
    """
    It takes the data from the form, creates a message with it, and sends it to the designated mail address
    :return: the redirect function.
    """

    if request.method == "POST":
        # fetching data
        nom: str = request.form.get("nom")
        prenom: str = request.form.get("prenom")
        telephone: str = request.form.get("téléphone")
        motivations: str = request.form.get("motivations")
        mail: str = request.form.get("mail")
        annee: str = request.form.get("annee_etude")

        # mail connection informations
        sender_email = "devis@jinnov-insa.fr"
        receiver_email = "axel.lenroue@jinnov-insa.fr"
        connection_token = ""

        # message creation
        message = f"""
            Nom et prenom du contact = {nom} {prenom}
        Mail de contact = {mail}
        Téléphone = {telephone}
        Année d'étude = {annee}
        Motivations = {motivations} """

        # mail creation
        msg = EmailMessage()
        msg["MIME-Version"] = "1.0"
        msg["Subject"] = str("candidature " + str(nom))
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(message)

        message = str(msg)
        send_mail(message, sender_email, receiver_email, connection_token)
        return redirect("/")
