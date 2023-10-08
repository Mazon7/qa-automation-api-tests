import random
import string

# # printing letters
letters = string.ascii_letters
name = 'Offer_' + "".join(random.choice(letters) for i in range(10))


class OfferData:
    data = {
        "name": name,
        "catalog_id": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "is_promocode_allowed": False,
        "is_active": True,
        "prices": [
            {
                "cost": 344554,
                "currency": "USD"
            }
        ],
        "description": "This is the test tariff",
        "reward_percent": None,
        "fix_remuneration": 4
    }

    # Change all values except of prices
    data_updated = {
        "name": name + "Updated",
        "catalog_id": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "is_promocode_allowed": True,
        "is_active": False,
        "prices": [
            {
                "cost": 500000,
                "currency": "RUB"
            }
        ],
        "description": "This is the Updated test tariff",
        "fix_remuneration": 3
    }

    # ADD Price
    part_data_updated = {
        "prices": [
            {
                "cost": 500000,
                "currency": "RUB"
            },
            {
                "cost": 200000,
                "currency": "USD"
            }
        ],
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
