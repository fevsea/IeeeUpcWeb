import smtplib
from datetime import time

import web.constants as Constants

from email.mime.text import MIMEText


def send(msg, subject='[IEEE_WEB] Contact from', fromaddr = 'admin@ieee.upc.edu'):
    toaddrs = 'alejandro.a.es@ieee.org'
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    # The actual mail send
    smtp = smtplib.SMTP("localhost")
    smtp.send_message(msg)
    smtp.quit()