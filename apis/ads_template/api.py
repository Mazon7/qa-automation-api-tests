import logging
from jsonschema import validate

from apis.requests import Client
from apis.ads_template.model import ResponseModel

logger = logging.getLogger("api")


class AdsTemplate:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'ads_template/'

    def get_templates(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_template(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
