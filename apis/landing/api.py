import logging
from jsonschema import validate

from apis.requests import Client
from apis.landing.model import ResponseModel

logger = logging.getLogger("api")


class Landing:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'landing/'
    LANDING_BY_CATALOG = "get_landing_by_catalog/"

    def create_landing(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_ROUTE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_landing(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PUT", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def part_upd_landing(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def delete_landing(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "DELETE", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response)
        return ResponseModel(status=response.status_code, response=response)

    def get_landing_catalog(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/{self.LANDING_BY_CATALOG}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
