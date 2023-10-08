import logging
from jsonschema import validate

from apis.requests import Client
from apis.promo.model import ResponseModel

logger = logging.getLogger("api")


class Postback:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'postback/'
    TEMPLATES = MAIN_ROUTE + 'get_postback_templates/'
    URL = MAIN_ROUTE + 'test_postback_url/'
    FIELD_ENUM = 'postback_field_enum/'

    def get_postback_list(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}?page=1&page_size=10", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def create_postback(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_ROUTE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_postback(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_postback(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PUT", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_postback(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "DELETE", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)

    def get_postback_templates(self,  headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.TEMPLATES}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def check_postback_url(self, url: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.URL}{url}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def postback_field_enum(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.FIELD_ENUM}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
