# This is a Python Program that automates the Gmail app to send automatic replies to unread mails that it recieves

from bot import get_mail_reply
# First we have to import the imaplib
import imaplib

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import email


from bardapi import Bard
import os
from dotenv import load_dotenv

host = "imap.gmail.com"
myEmail = "user_mail"
myPassword = "user_password" # Note: You need to get your 8 Characters App Passwords that Google generates after two factor verification


def main():
    while True:
        try:
            get_inbox()
        except KeyboardInterrupt:
            break


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(myEmail, myPassword)
    mail.select("inbox")

    _, searched_data = mail.search(None, 'Unseen')

    for searched in searched_data[0].split():

        _, mail_data = mail.fetch(searched, "(RFC822)")
        
        # print(mail_data)
        _, data = mail_data[0]

        message = email.message_from_bytes(data)

        email_sender = message["From"]

        for msg_part in message.walk():
            if msg_part.get_content_type() == "text/plain":
                email_msg_body = msg_part.get_payload(decode=False)

        get_data(email_sender, email_msg_body)

    mail.logout()


def get_data(email_sender, email_msg_body):
    starting_index = email_sender.index("<") + 1
    ending_index = email_sender.index(">")

    email_address = email_sender[starting_index: ending_index]
    email_sender_name = email_sender[ :starting_index - 2]

    send_email(email_sender_name, email_address, email_msg_body)


def send_email(email_sender_name, email_address, email_msg_body):
    sender = myEmail

    receiver = email_address
    subject = '' # your_subject here
    body = get_mail_reply(email_msg_body, email_sender_name)
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(myEmail, myPassword)
    server.send_message(message)

    server.quit()

if __name__ == "__main__":
    main()