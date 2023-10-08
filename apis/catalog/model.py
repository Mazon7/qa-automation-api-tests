import random
import string

# printing letters
letters = string.ascii_letters
catalog_code = 'test_' + "".join(random.choice(letters) for i in range(10))


class CreateCatalog:
    data = {
        "title": "NewTestCatalog",
        "catalog_code": catalog_code,
        "hold_duration": "30 00:00:00",
        "canceled_duration": "14 00:00:00",
        "is_promocode_allowed": False,
        "preview_image": "https://picsum.photos/200",
        "description": "TestDescription",
        "reward_type": "RevShare",
        "devices": "All",
        "cookies_storage_days": 2147483647,
        "max_promo_code_percent": 9,
        "is_confirmed": True,
        "is_published": True,
        "min_promo_code_percent": 7
    }

    updated_data = {
        "title": "Test Catalog QA",
        "catalog_code": catalog_code,
        "hold_duration": "40 00:00:00",
        "canceled_duration": "20 00:00:00",
        "is_promocode_allowed": True,
        "preview_image": "https://picsum.photos/300",
        "description": "UpdatedTestDescription",
        "reward_type": "RevShare",
        "devices": "All",
        "cookies_storage_days": 2147483647,
        "max_promo_code_percent": 10,
        "is_confirmed": False,
        "is_published": False,
        "min_promo_code_percent": 10
    }

    part_updated_data = {
        "title": "Test Catalog QA",
        "catalog_code": "test_catalog",
        "hold_duration": "40 00:00:00",
        "canceled_duration": "20 00:00:00",
        "is_promocode_allowed": True,
        "preview_image": "https://picsum.photos/300",
        "description": "UpdatedTestDescription",
        "reward_type": "RevShare",
        "devices": "All",
        "cookies_storage_days": 2147483647,
        "max_promo_code_percent": 20,
        "is_confirmed": False,
        "is_published": False,
        "min_promo_code_percent": 5
    }

    catalog_for_promo = {
        "title": "NewTestCatalog",
        "catalog_code": "Promo_" + catalog_code,
        "hold_duration": "30 00:00:00",
        "canceled_duration": "14 00:00:00",
        "is_promocode_allowed": False,
        "preview_image": "https://picsum.photos/200",
        "description": "TestDescription",
        "reward_type": "RevShare",
        "devices": "All",
        "cookies_storage_days": 2147483647,
        "max_promo_code_percent": 9,
        "is_confirmed": True,
        "is_published": True,
        "min_promo_code_percent": 7
    }

    set_rule_data = {
        "WEBSITE": True,
        "ONION_SITE": True,
        "FORUM": True,
        "WHITE_DOORWAYS": True,
        "GRAY_DOORWAYS": True,
        "BLACK_DOORWAYS": True,
        "CASHBACK": True,
        "NOTICE_BOARDS": True,
        "CONTEXTUAL_ADVERTISING": True,
        "CONTEXTUAL_ADVERTISING_ON_THE_BRAND": True,
        "EMAIL": True,
        "SMS": True,
        "TEASER_ADVERTISING": True,
        "BANNER_ADVERTISING": True,
        "PUSH_NOTIFICATIONS": True,
        "CLICK_UNDER": True,
        "POP_UP": True,
        "POP_UNDER": True,
        "TOOLBAR": True,
        "TARGETED_ADVERTISING_IN_SOCIAL_MEDIA": True,
        "TELEGRAM_ADS": True,
        "VIDEO_ADS": True,
        "NATIVE_ADVERTISING": True,
        "MOTIVATED_TRAFFIC": True,
        "MOBILE_TRAFFIC": True,
        "PWA": True,
        "ADULT_TRAFFIC": True
    }


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response
