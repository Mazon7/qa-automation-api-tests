import random
import string


letters = string.ascii_letters
name = 'Promo_' + "".join(random.choice(letters) for i in range(10))


class PromoData:
    data = {
        "code": name,
        "percent_discounts": 15,
        "catalog": ["9bce21ea-c8da-43e7-a563-ee05f22c1ed6"]
    }

    data_updated = {
        "code": name + "Updated",
        "percent_discounts": 10,
        "catalog": ["9bce21ea-c8da-43e7-a563-ee05f22c1ed6", "77e43d94-c338-43ab-a45f-b31483957e00"]
    }

    part_data_updated = {"percent_discounts": 7}

    bp_promo_data = {
        "percent_discounts": "10",
        "user": "test@example.com",
        "code": name
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
