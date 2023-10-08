import logging
from jsonschema import validate

from apis.requests import Client
from apis.promo.model import ResponseModel

logger = logging.getLogger("api")


class Promo:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'promo/'
    CHECK_PROMO = MAIN_ROUTE + 'check_promo/'
    CHECK_BY_PROMO = MAIN_ROUTE + 'check_promo_by_code/'
    CHECK_PROMO_UUID = MAIN_ROUTE + 'check_uuid/'
    CREATE_PROMO = MAIN_ROUTE + 'create_promo_for_user/'
    CREATE_PREFIX = MAIN_ROUTE + 'prefix_promo_code/'

    def create_promo(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_ROUTE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_promo(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_promo(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PUT", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def part_upd_promo(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def check_promo(self, catalog_id: str, code: str,  headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.CHECK_PROMO}?catalog_id={catalog_id}&code={code}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def check_promo_bycode(self, catalog_code: str, code: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.CHECK_BY_PROMO}?catalog_code={catalog_code}&code={code}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def check_uuid(self, user_id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.CHECK_PROMO_UUID}?code={user_id}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def create_promo_user(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.CREATE_PROMO}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def create_promo_prefix(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.CREATE_PREFIX}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
