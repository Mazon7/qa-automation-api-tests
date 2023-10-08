import random
import string

# printing letters
letters = string.ascii_letters
name = 'Rule_' + "".join(random.choice(letters) for i in range(10))


class TextRuleData:
    data = {
        "text": name,
        "language": "RU",
        "catalog": "9bce21ea-c8da-43e7-a563-ee05f22c1ed6"
    }
    data_updated = {
        "text": name + "Updated",
        "language": "EN",
        "catalog": "9bce21ea-c8da-43e7-a563-ee05f22c1ed6"
    }
    part_data_updated = {"language": "RU"}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
