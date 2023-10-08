import random
import string

# printing letters
letters = string.ascii_letters
name = 'data_' + "".join(random.choice(letters) for i in range(10))


class LinkConstructorData:
    data = {
        "domain": "TYLKNPF9",
        "landing": "RC5WUB",
        "ads_template": "UZH0LV",
        "subid": "subid",
        "subid1": "subid1",
        "subid2": "subid2",
        "subid3": "subid3",
        "subid4": "subid4",
        "subid5": "subid5",
        "subid6": "subid6",
        "subid7": "subid7",
        "subid8": "subid8",
        "subid9": "subid9",
        "subid10": "subid10",
        "subid11": "subid11",
        "subid12": "subid12",
        "subid13": "subid13",
        "subid14": "subid14",
        "subid15": "subid15",
        "subid16": "subid16",
        "subid17": "subid17",
        "subid18": "subid18"
    }

    data_updated = {
        "domain": "FDQKEPIC",
        "landing": "ZX3H15",
        "ads_template": "QBF0H3",
        "subid": "subid_Updated",
        "subid1": "subid1_Updated",
        "subid2": "subid2_Updated",
        "subid3": "subid3_Updated",
        "subid4": "subid4_Updated",
        "subid5": "subid5_Updated",
        "subid6": "subid6_Updated",
        "subid7": "subid7_Updated",
        "subid8": "subid8_Updated",
        "subid9": "subid9_Updated",
        "subid10": "subid10_Updated",
        "subid11": "subid11_Updated",
        "subid12": "subid12_Updated",
        "subid13": "subid13_Updated",
        "subid14": "subid14_Updated",
        "subid15": "subid15_Updated",
        "subid16": "subid16_Updated",
        "subid17": "subid17_Updated",
        "subid18": "subid18_Updated"
    }

    part_data_updated = {"subid": "subid_Updated_New"}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
