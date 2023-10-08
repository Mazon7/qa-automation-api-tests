import random
import string

# printing letters
letters = string.ascii_letters
name = 'Promo_' + "".join(random.choice(letters) for i in range(10))


class MaterialData:
    data = {
        "url": "https://example.com/",
        "type_material": "URL",
        "catalog": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "title": "Test_Material"
    }
    data_updated = {
        "url": "https://picsum.photos/200",
        "type_material": "IMAGE",
        "catalog": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "title": "Test_Material_Updated"
    }

    part_data_updated = {"type_material": "FILE"}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
