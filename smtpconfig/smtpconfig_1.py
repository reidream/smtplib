import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, "gmail.env")

load_dotenv(env_path)
from_ = os.getenv("From_Address")
key_ = os.getenv("Key")

SMTP_CONFIG_1={
    'smtp_server': 'smtp.gmail.com',
    'port': 587,
    'sender_email': from_,
    'password': key_
}