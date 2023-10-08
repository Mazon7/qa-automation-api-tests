import random
import string

# # printing letters
letters = string.ascii_letters
random_name = 'Deal_' + "".join(random.choice(letters) for i in range(10))


class DealData:
    params = {"conversion_time_after": "", "conversion_time_before": "10",
              "currency": ["Test"], "O": ["-conversion_time", ""], "offer": ["Test"], "page": 10, "page_size": 7, "promo": ["data"], "status": ["Approved"]}

    data = {
        "status": "Created",
        "offer": "Test Offer QA",
        "cost": "13333",
        "promo_code": "N85BA9XRLDTO",
        "currency": "USD",
        "is_returned": False,
        "deal_id": random_name,
        "catalog_code": "test_catalog"
    }
    # ONE OF THE REQUIRED FIELS
    # promo_code is unique inside one catalog
    # "promo_code": "string"
    # OR
    # "another_data": "string" --> myshare=JU8KDCYF&subid=Product1
    # Product1 --> parameter for arbitrage

    data_updated = {
        "status": "Paid",
        "cost": "10000",
        "is_returned": False,
        "comment": "NewString"
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
