from email.message import EmailMessage
from smtplib import SMTP
from os import environ
from dotenv import load_dotenv
import sys


load_dotenv()
email = environ['EMAIL']
pw =  environ['PW']


def send_email(subject='No subject', content='No content', **kwargs) -> dict:
    
    message = EmailMessage()
    message['from'] = email
    message['to'] = email
    message['subject'] = subject
    message.set_content(content, **kwargs)

    with SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(email, pw)
        failure = server.send_message(message)

    return failure




if __name__ == '__main__':
    send_email()