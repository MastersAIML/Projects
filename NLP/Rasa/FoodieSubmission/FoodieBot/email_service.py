import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmail(from_address, password, to_address, subject, body_msg):
    """Responsible to send mails"""
    #Data preparation
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body_msg, 'plain'))

    #Server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from_address, password)

    #Send mail
    server.sendmail(from_address, to_address.split(","), msg.as_string())

    #Quit server
    server.quit()