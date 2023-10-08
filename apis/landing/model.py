import random
import string

# # printing letters
letters = string.ascii_letters
random_name = 'Landing_' + "".join(random.choice(letters) for i in range(10))


class LandingData:
    data = {
        "url": "https://example.com/",
        "adaptability": "All",
        "title": "Test Landing",
        "catalog_id": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "image_url": "https://picsum.photos/200"
    }
    data_updated = {
        "url": "https://example.com/test",
        "adaptability": "Desktop",
        "title": "Test Landing Updated",
        "catalog_id": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "image_url": "https://picsum.photos/300"
    }
    data_part_updated = {
        "adaptability": "Mobile",
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
