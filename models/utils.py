import smtplib
import os
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

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(sender_email, connection_token)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()


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
        sender_email = os.getenv("MAIL_DEVIS_USERNAME")
        receiver_email = os.getenv("MAIL_DEVIS_RECIPIENT")
        connection_token = os.getenv("MAIL_DEVIS_PASSWORD")

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
        sender_email = os.getenv("MAIL_STUDENT_USERNAME")
        receiver_email = os.getenv("MAIL_STUDENT_RECIPIENT")
        connection_token = os.getenv("MAIL_STUDENT_PASSWORD")

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
