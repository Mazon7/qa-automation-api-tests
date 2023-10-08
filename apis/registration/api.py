import logging
from jsonschema import validate

from apis.requests import Client
from apis.registration.model import ResponseModel

logger = logging.getLogger("api")


class User:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_PATH_USER = 'auth/users/'
    POST_ACTIVATE_USER = MAIN_PATH_USER + 'activation/'
    GET_REFERRAL_URL = MAIN_PATH_USER + 'get_referral_url/'
    GET_USER_INFO = MAIN_PATH_USER + 'me/'
    RESEND_ACTIVATION = MAIN_PATH_USER + 'resend_activation/'
    RESET_PASSWORD = MAIN_PATH_USER + 'reset_password/'
    RESET_PASSWORD_CONFIRM = MAIN_PATH_USER + 'reset_password_confirm/'
    CHANGE_PASSWORD = MAIN_PATH_USER + 'set_password/'
    DELETE_USER = MAIN_PATH_USER + 'me/'


    def register_user(self, body: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_PATH_USER}", json=body)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def activate_user(self, body: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.POST_ACTIVATE_USER}", json=body)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code)

    def get_ref_url(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_REFERRAL_URL}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)

    def get_user_info(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_USER_INFO}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response.json())

    def resend_activation(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.RESEND_ACTIVATION}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)

    def reset_password(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.RESET_PASSWORD}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)

    def reset_password_confirm(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.RESET_PASSWORD_CONFIRM}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        logger.info(response.text)

        return ResponseModel(status=response.status_code, response=response)

    def change_password(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.CHANGE_PASSWORD}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response)

    def delete_user(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "DELETE", f"{self.url}{self.DELETE_USER}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response)
