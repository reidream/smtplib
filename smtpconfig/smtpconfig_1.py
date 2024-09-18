import os
from dotenv import load_dotenv

load_dotenv("smtpconfig/gmail.env")
from_ = os.getenv("From_Address")
key_ = os.getenv("Key")

SMTP_CONFIG_1={
    'smtp_server': 'smtp.gmail.com',
    'port': 587,
    'sender_email': from_,
    'password': key_
}