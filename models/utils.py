import smtplib, ssl

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
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email,  connection_token)
        server.sendmail(sender_email, receiver_email, message)
