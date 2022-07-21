import smtplib, ssl
from flask import *
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart

def mail_manager(message:str, sender_email:str, receiver_email:str, connection_token:str):
    """
    This function sends an email to the receiver_email address with the message.
    
    :param message: The message to be sent
    :param sender_email: The email address of the sender
    :param receiver_email: The email address of the person you want to send the email to
    :param connection_token: This is the application token of the email address you're sending from
    """
    port = 465
    smtp_server = "smtp.gmail.com"
    print(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email,  connection_token)
        server.sendmail(sender_email, receiver_email, message)

def Mail_devis_create():
    """
    It takes the data from the form, creates a message with it, and sends it to the designated mail address
    :return: the redirect function.
    """

    #fetching data
    if request.method == 'POST':
        nom_entreprise:str = request.form.get('nom_entreprise')
        nom:str = request.form.get('nom')
        prenom:str = request.form.get('prenom')
        adresse:str = request.form.get('Adresse')
        telephone:str = request.form.get('téléphone')
        contenu:str =request.form.get('contenu')
        mail:str =request.form.get('mail')

        #message creation
        message = f"""
            Nom de l'entreprise = {nom_entreprise}
            Nom et prenom du contact = {nom} {prenom}
            Adresse de l'entreprise (optionnel) = {adresse}
            Mail de contact = {mail}
            Téléphone = {telephone}
            Demande =  \n{contenu}
            """

        #mail connection informations
        sender_email = 'jn.bonvent@gmail.com'
        receiver_email = 'bonvent.jn@gmail.com'
        connection_token = 'undzgoozsfvczgcx'

        #mail creation
        msg = EmailMessage()
        msg['MIME-Version'] = '1.0'
        msg['Subject'] = str('demande de devis ' + nom_entreprise)
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(message)

        message = str(msg)
            
        mail_manager(message, sender_email, receiver_email, connection_token)
        return redirect('/')

def Mail_student_create():
    """
    It takes the data from the form, creates a message with it, and sends it to the designated mail address
    :return: the redirect function.
    """
    
    if request.method == 'POST':
        #fetching data
        nom:str = request.form.get('nom')
        prenom:str = request.form.get('prenom')
        telephone:str = request.form.get('téléphone')
        motivations:str =request.form.get('motivations')
        post:str =request.form.get('Post')
        mail:str =request.form.get('mail')

        #mail connection informations
        sender_email = 'jn.bonvent@gmail.com'
        receiver_email = 'jn.bonvent@gmail.com'
        connection_token = 'undzgoozsfvczgcx'

        #message creation
        message = f"""
            Nom et prenom du contact = {nom} {prenom}
        Mail de contact = {mail}
        Téléphone = {telephone}
        Poste = {post}
        Motivations = {motivations} """

        #mail creation
        msg = EmailMessage()
        msg['MIME-Version'] = '1.0'
        msg['Subject'] = str('candidature ' + str(nom))
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(message)

        message = str(msg)
        print('1')
        mail_manager(message, sender_email, receiver_email, connection_token)
        return redirect('/')
