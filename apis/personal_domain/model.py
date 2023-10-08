class DomainData:
    data = {"domain": "Test_Domain"}

    data_updated = {"domain": "Test_Domain_Updated"}

    part_data_updated = {"domain": "Test_Domain_Updated_New"}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
