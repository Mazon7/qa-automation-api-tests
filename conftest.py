import pytest

from apis.auth.model import AuthUser
from apis.auth.api import Auth
from apis.schemas.register import valid_schema


from apis.offer.model import OfferData
from apis.offer.api import Offer

from apis.catalog.model import CreateCatalog
from apis.catalog.api import Catalog

from apis.business_partner.api import BusinessPartner

from constants import URL, QA_EMAIL, QA_PASSWORD


def pytest_configure(config):
    # register your new marker to avoid warnings
    config.addinivalue_line(
        "markers",
        "key: specify a test key"
    )


def pytest_addoption(parser):
    # add your new filter option (you can name it whatever you want)
    parser.addoption('--key', action='store')


def pytest_collection_modifyitems(config, items):
    # check if you got an option like --key=test-001
    filter = config.getoption("--key")
    if filter:
        new_items = []
        for item in items:
            mark = item.get_closest_marker("key")
            if mark and mark.args and mark.args[0] == filter:
                # collect all items that have a key marker with that value
                new_items.append(item)
        items[:] = new_items


# Get Authorization tokens
@pytest.fixture
def get_auth_tokens(user=QA_EMAIL, password=QA_PASSWORD):
    body = AuthUser.get_body(user, password)
    response = Auth(url=URL).get_jwt(body=body, schema=valid_schema)
    return response.response


# Get Refresh Authorization token
# DO NOT USE THIS ROUTE, UNTIL ROUTE FOR GETTING TOKEN EXISTS
# @pytest.fixture
# def get_refresh_token(get_auth_tokens):
#     response = BusinessPartner(url=URL).get_refresh_token(headers={
#         "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
#     return response.response


# @pytest.fixture
def get_tariff_id(get_auth_tokens):
    response = Offer(url=URL).create_offer(body=OfferData.data, headers={
        "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
    return response.response["id"]


@pytest.fixture
def get_catalog_id(get_auth_tokens):
    response = Catalog(url=URL).create_catalog(body=CreateCatalog.catalog_for_promo, headers={
        "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
    # return None
    return response.response["id"]

class OfferValueStorage:
    id = None

class LandingValueStorage:
    id = None

class DomainValueStorage:
    id = None

class PromoValueStorage:
    id = None

class MaterialValueStorage:
    id = None

class TextRuleValueStorage:
    id = None

class LinkConstValueStorage:
    id = None

class PostbackValueStorage:
    id = None

class CatalogIdValueStorage:
    id = None