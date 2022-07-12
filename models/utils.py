import smtplib, ssl

def mail_manager(message):
    """Procedure envoyant un e-mail vers une boite mail dédié"""

    port = 465 
    smtp_server = "smtp.gmail.com"
    sender_email = "mail"  # Enter your address
    receiver_email = "mail"  # Enter receiver address
    password = "token" #mdp d'application généré depuis google


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
