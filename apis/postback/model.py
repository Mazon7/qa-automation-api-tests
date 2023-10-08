from constants import URL_QA



class PostbackData:
    data = {
        "name": "TestPostback",
        "url": f"{URL_QA}tools/new_postback/",
        "user_url": f"{URL_QA}tools/new_postback/?qw=uid",
        "status": [
            "Created"
        ],
        "postback_field": [
            {
                "key": "subid",
                "value": "click_id"
            }
        ],
        "catalog": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "postback_template": "DS6N1H"
    }

    data_updated = {
        "name": "TestPostbackUpdated",
        "url": f"{URL_QA}tools/new_postback_updated",
        "user_url": f"{URL_QA}tools/new_postback/?qw=uid",
        "status": [
            "Created", "Approved"
        ],
        "postback_field": [
            {
                "key": "subid",
                "value": "click_id"
            },
            {
                "key": "subid_1",
                "value": "click_id_1"
            }
        ],
        "catalog": "5420dbef-423b-4f2c-af1e-b179041ff010",
        "postback_template": "12ZU05"
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
