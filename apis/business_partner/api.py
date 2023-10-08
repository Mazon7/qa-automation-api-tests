import logging
from jsonschema import validate

from apis.requests import Client
from apis.business_partner.model import ResponseModel

logger = logging.getLogger("api")


class BusinessPartner:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    MAIN_ROUTE = 'business_partner/'
    GET_CATALOG = 'retrieve_catalog/'
    GET_CATALOGS = MAIN_ROUTE + 'catalog/'
    GET_DEALS = MAIN_ROUTE + "get_list_deals/"
    GET_PARTNERS = MAIN_ROUTE + "get_list_partners/"
    GET_STAT = MAIN_ROUTE + "get_statistic_by_company/"
    GET_EXPENSES = MAIN_ROUTE + "get_story_expenses/"
    TOKEN = MAIN_ROUTE + "refresh_business_token/"
    BUSINESS_PARTNER = MAIN_ROUTE + "setting_business_partner/"

    def get_bp_info(self, params: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}", params=params, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_bp_catalog(self, id: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.MAIN_ROUTE}{id}/{self.GET_CATALOG}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_all_catalogs(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_CATALOGS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_list_deals(self, params: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_DEALS}{params}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_partners(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_PARTNERS}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_stat(self, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_STAT}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_expenses(self, params: str, headers: dict, schema: dict):
        response = self.client.custom_request(
            "GET", f"{self.url}{self.GET_EXPENSES}{params}", headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def get_refresh_token(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.TOKEN}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())

    def set_business_partner(self, body: dict, headers: dict, schema: dict):
        response = self.client.custom_request(
            "PATCH", f"{self.url}{self.BUSINESS_PARTNER}", json=body, headers=headers)
        # validate(instance=response.json(), schema=schema)
        logger.info(response.json())
        return ResponseModel(status=response.status_code, response=response.json())
