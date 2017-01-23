import smtplib
from datetime import time

import web.constants as Constants

from email.mime.text import MIMEText


def send(msg, subject='[IEEE_WEB] Contact from', fromaddr = 'aagustinb@gmail.com'):
    toaddrs = 'alejandro.a.es@ieee.org'
    username = 'aagustinb@gmail.com'
    password = Constants.mailPasswrd

    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddrs

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()