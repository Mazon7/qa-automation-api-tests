import logging
from jsonschema import validate

from apis.requests import Client
from apis.deals.model import ResponseModel

logger = logging.getLogger("api")


class Deals:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'deal/'
    COUNT_DEALS = MAIN_ROUTE + "get_count_deals/"
    GEN_STAT_DEALS = MAIN_ROUTE + "get_general_statistics_deals/"
    STAT_USER_DEALS = MAIN_ROUTE + "get_general_statistics_user_deals/"
    PARAMS_WITH_DEALS = MAIN_ROUTE + "get_params_with_deals/"
    STAT_DEALS = MAIN_ROUTE + "get_statistics_deals/"

    def get_deals(self, parameter: str, value: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}?{parameter}={value}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def create_deal(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "POST", f"{self.url}{self.MAIN_ROUTE}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_deal(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def update_deal(self, body: dict, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.MAIN_ROUTE}{id}/", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_count_deals(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.COUNT_DEALS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def gen_stat_deals(self, params, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GEN_STAT_DEALS}", params=params, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_stat_user_deals(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.STAT_USER_DEALS}?group_by=cid", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_params_deals(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.PARAMS_WITH_DEALS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_stat_deals(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.STAT_DEALS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
