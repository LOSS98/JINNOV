import smtplib

fromaddr = 'devis@jinnov-insa.fr'
toaddrs  = 'axel.lenroue@jinnov-insa.fr'
msg = "Test"
username = 'devis@jinnov-insa.fr'
password = 'mkgzrnmynruniivj' # Here
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()