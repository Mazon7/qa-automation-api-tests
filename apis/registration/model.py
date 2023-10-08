from faker import Faker
from pymailtm import MailTm, Account
import re


fake = Faker()
mt = MailTm().get_account()  # create temp email
random_pass = fake.password()  # create random password


class RegisterUser:
    @staticmethod
    # Create Temp Email for Activation
    def get_temp_email():
        return {"id": mt.id_, "email": mt.address, "password": mt.password}

    @staticmethod
    def get_messages():
        messages = Account(mt.id_, mt.address, mt.password).get_messages()
        return messages

    @staticmethod
    def get_activation_data():
        messages = Account(mt.id_, mt.address, mt.password).get_messages()
        message = messages[1]
        # REGEX #
        regex = r'https://qa.myshare.systems/activate/\S+(?=\])'
        link = re.findall(regex, message.text)
        data = link[0].split("/")[-2:]
        return data[0], data[1]

    @staticmethod
    def get_reset_password_data():
        messages = Account(mt.id_, mt.address, mt.password).get_messages()
        message = messages[0]
        # REGEX #
        regex = r'https://qa.myshare.systems/password-reset/confirm/\S+(?=\])'
        link = re.findall(regex, message.text)
        data = link[0].split("/")[-2:]
        print(data)
        return data[0], data[1]

    @ staticmethod
    def random():
        # fake.email()
        email = mt.address
        password = random_pass
        email_newsletter = True
        referral = "string"
        telegram_username = "string"
        print(email, password, email_newsletter,
              referral, telegram_username)
        return {"email": email, "password": password, "email_newsletter": email_newsletter, "referral": referral, "telegram_username": telegram_username}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
