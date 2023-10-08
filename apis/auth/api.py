import logging
from jsonschema import validate

from apis.requests import Client
from apis.auth.model import ResponseModel

logger = logging.getLogger("api")


class Auth:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_AUTH = 'auth/jwt/'
    GET_JWT_TOKEN = MAIN_AUTH + 'create/'  # Login user
    VERIFY_JWT_TOKEN = MAIN_AUTH + 'verify/'
    REFRESH_JWT_TOKEN = MAIN_AUTH + 'refresh/'
    LOGOUT = MAIN_AUTH + 'logout/'  # Logout user

    def get_jwt(self, body: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.GET_JWT_TOKEN}", json=body)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def verify_jwt(self, body: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.VERIFY_JWT_TOKEN}", json=body)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def refresh_jwt(self, body: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.REFRESH_JWT_TOKEN}", json=body)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def log_out(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.LOGOUT}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        # THIS API REQUEST DOESN'T HAVE RESPONSE BODY
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)
