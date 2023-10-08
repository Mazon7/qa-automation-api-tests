import logging
from jsonschema import validate

from apis.requests import Client
from apis.catalog.model import ResponseModel

logger = logging.getLogger("api")


class Catalog:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    CATALOG = 'catalog/'
    ADD_USER = "add_user_to_catalog/"
    SET_RULE = "setting_rule_traffic/"
    GET_CATALOG = CATALOG + "get_catalog/"
    GET_CATALOG_USER = CATALOG + "get_catalog_by_user/"
    GET_CATALOG_DEALS = CATALOG + "get_catalog_with_deals/"
    GET_CATALOG_OFFERS = CATALOG + "get_offer_with_deals/"

    def get_catalogs(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.CATALOG}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, response=response.json())

    def create_catalog(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.CATALOG}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_catalog(self, uid: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.CATALOG}{uid}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_catalog(self, uid: str, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PUT", f"{self.url}{self.CATALOG}{uid}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def part_update_catalog(self, uid: str, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.CATALOG}{uid}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def add_user_catalog(self, uid: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.CATALOG}{uid}/{self.ADD_USER}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def set_rule_traffic(self, uid: str, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.CATALOG}{uid}/{self.SET_RULE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_catalog_by_code(self, catalog_code: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_CATALOG}?catalog_code={catalog_code}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_catalog_by_user(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_CATALOG_USER}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_catalog_with_deals(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_CATALOG_DEALS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_offer_with_deals(self, catalogs: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_CATALOG_OFFERS}?list_catalogs={catalogs}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
