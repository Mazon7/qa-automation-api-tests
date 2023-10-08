import logging
from jsonschema import validate

from apis.requests import Client
from apis.link_constructor.model import ResponseModel

logger = logging.getLogger("api")


class LinkConstructor:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'link_constructor/'

    def create_link_constructor(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_ROUTE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_link_constructor(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_link_constructor(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PUT", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def part_upd_link_constructor(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_link_constructor(self, id: str,  headers: dict, schema: dict):
        response = self.client.custom_request(
            "DELETE", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)
