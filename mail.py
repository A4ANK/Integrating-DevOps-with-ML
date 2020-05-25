#!/usr/bin/python3

import smtplib, ssl
#import getpass  # to take secured stdin for password

port = 587  # Port for starttls
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = "Type your password and press enter"
message = """
Subject: Notice

This message is sent from Python.
"""
try:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
   
#except Exception as err:
#   print('Error Occured : ', err)
except:
    print("Error occurred")
else:
    print("Mail has been sent successfully")