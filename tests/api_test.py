from apis.registration.api import User
from apis.registration.model import RegisterUser
from apis.schemas.register import valid_schema

from apis.business_partner.api import BusinessPartner
from apis.business_partner.model import BusinessPartnerData

from apis.auth.api import Auth
from apis.auth.model import AuthUser

from apis.catalog.api import Catalog
from apis.catalog.model import CreateCatalog

from apis.offer.api import Offer
from apis.offer.model import OfferData

from apis.deals.api import Deals
from apis.deals.model import DealData

from apis.landing.api import Landing
from apis.landing.model import LandingData

from apis.personal_domain.api import PersonalDomain
from apis.personal_domain.model import DomainData

from apis.promo.api import Promo
from apis.promo.model import PromoData

from apis.promo_material.api import PromoMaterial
from apis.promo_material.model import MaterialData

from apis.text_rule.api import TextRule
from apis.text_rule.model import TextRuleData

from apis.ads_template.api import AdsTemplate


from apis.link_constructor.api import LinkConstructor
from apis.link_constructor.model import LinkConstructorData


from apis.postback.api import Postback
from apis.postback.model import PostbackData


from conftest import OfferValueStorage, LandingValueStorage, DomainValueStorage, PromoValueStorage, MaterialValueStorage, TextRuleValueStorage, LinkConstValueStorage, PostbackValueStorage, CatalogIdValueStorage

import allure
import pytest
from collections.abc import Iterable
import random
import string

from constants import QA_EMAIL, QA_PASSWORD, URL, AUTH_TOKEN, TEST_PASS


TEMP_EMAIL_CREDS = RegisterUser.get_temp_email()

# Helper functions
def get_tokens(user=QA_EMAIL, password=QA_PASSWORD):
    body = AuthUser.get_body(user, password)
    response = Auth(url=URL).get_jwt(body=body, schema=valid_schema)
    return response.response

# End of helper functions


@allure.feature('Business Partner')
class TestBusinessPartner:
    @pytest.mark.get_bp_info
    def test_get_bp_info(self):
        response = BusinessPartner(url=URL).get_bp_info(params="?page=1&page_size=10", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("domain")

    @pytest.mark.get_bp_catalog
    def test_get_bp_catalog(self):
        response = BusinessPartner(url=URL).get_bp_catalog(id="0d4d29e4-b755-4029-8045-94482aaf954c", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("catalog_id")
        assert resp.get("title")
        assert resp.get("catalog_code")
        assert isinstance(resp.get("offers"), Iterable)
        assert resp.get("hold_duration")
        assert resp.get("canceled_duration")
        assert resp.get("is_promocode_allowed")
        assert resp.get("category")
        assert resp.get("approval_rate")
        assert resp.get("company_name")
        assert isinstance(resp.get("offer_geo"), Iterable)
        assert resp.get("preview_image") == None
        assert resp.get("company_logo")
        assert resp.get("description")
        assert resp.get("reward_type")
        assert isinstance(resp.get("rules"), dict)
        assert isinstance(resp.get("text_rule"), Iterable)
        assert resp.get("devices")
        assert isinstance(resp.get("localizations"), Iterable)
        assert isinstance(resp.get("promo_materials"), Iterable)
        assert isinstance(resp.get("landings"), Iterable)
        assert resp.get("is_confirmed")
        assert resp.get("is_published")
        assert resp.get("max_promo_code_percent")
        assert resp.get("min_promo_code_percent")
        assert resp.get("moderation_type")

    @pytest.mark.get_bp_catalogs
    def test_get_bp_catalogs(self):
        response = BusinessPartner(url=URL).get_all_catalogs(
            headers={"Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    # CHECK, NO DATA
    @pytest.mark.get_list_deals
    def test_get_list_deals(self):
        response = BusinessPartner(url=URL).get_list_deals(params='?catalog=0d4d29e4-b755-4029-8045-94482aaf954c', headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.get_partners
    def test_get_partners(self):
        response = BusinessPartner(url=URL).get_partners(headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.get_stat_company
    def test_get_stat(self):
        response = BusinessPartner(url=URL).get_stat(
            headers={"Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    # CHECK, NO DATA
    @pytest.mark.get_expenses
    def test_get_expenses(self):
        response = BusinessPartner(url=URL).get_expenses(params="", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.get_business_token
    @pytest.mark.skip(reason="THIS ROUTE IS NOT TESTED, BECAUSE IT CHANGES MAIN TOKEN!")
    def test_business_token(self):
        response = BusinessPartner(url=URL).get_refresh_token(body={"token": AUTH_TOKEN}, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.set_business_partner
    def test_business_partner(self):
        response = BusinessPartner(url=URL).set_business_partner(body={"company_logo": "https://picsum.photos/200", "displayed_company": "Test Company"}, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200


@allure.feature('Auth')
@allure.story('Auth API')
class TestAuth:
    @allure.title('Get access/refresh token')
    def test_get_auth(self):
        # If there are access & refresh tokens recieved
        # We assume that response code is 200
        token_resp = get_tokens()
        assert token_resp.get('access')
        assert token_resp.get('refresh')

    @allure.title('Verify access/refresh tokens')
    def test_verify_auth(self):
        token_resp = get_tokens()
        for token in [token_resp['access'], token_resp['refresh']]:
            response = Auth(url=URL).verify_jwt(
                body={"token": token}, schema=valid_schema)
            resp = response.response
            assert response.status == 200
            assert resp == {}

    @allure.title('Refresh access token')
    def test_refresh_auth(self):
        token_resp = get_tokens()
        response = Auth(url=URL).refresh_jwt(
            body={"refresh": token_resp['refresh']}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get('access')

    @allure.title('Logout user')
    def test_logout(self):
        token_resp = get_tokens()
        response = Auth(url=URL).log_out(body={"refresh":  token_resp['refresh']}, headers={
            "Authorization": f"Bearer {token_resp['access']}"}, schema=valid_schema)
        assert response.status == 205


@allure.feature('Users')
class TestUsers:
    @allure.title('Register user')
    def test_registration(self):
        body = RegisterUser.random()
        response = User(url=URL).register_user(
            body=body, schema=valid_schema)
        resp = response.response  # get response body from API
        assert response.status == 201
        assert resp.get('email')
        assert resp.get('email_newsletter')
        assert resp.get('referral') == None
        assert resp.get('telegram_username')
        assert not resp.get('password')  # check that password is not provided

    @allure.title('Resend activation email')
    def test_resend_activation(self):
        tokens_resp = get_tokens()
        email = TEMP_EMAIL_CREDS["email"]
        response = User(url=URL).resend_activation(body={"email": email}, headers={
            "Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
        # resp = response.response  # get response body from API
        assert response.status == 204

    @allure.title('Activate user')
    # Need to get email and use this email through the test
    def test_activation(self):
        uid, token = RegisterUser.get_activation_data()
        body = {'uid': uid, 'token': token}
        response = User(url=URL).activate_user(
            body=body, schema=valid_schema)
        assert response.status == 204

    @allure.title('Get Referral URL')
    def test_referral_url(self):
        tokens_resp = get_tokens()
        response = User(url=URL).get_ref_url(
            headers={"Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
        resp = response.response  # get response body from API
        assert response.status == 200
        assert resp.text == f'"{URL}ref/UFGSX3JM"'

    @allure.title('Get User Info')
    @pytest.mark.user_info
    def test_user_info(self):
        tokens_resp = get_tokens()
        response = User(url=URL).get_user_info(
            headers={"Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
        resp = response.response  # get response body from API
        assert response.status == 200
        assert resp.get('id')
        assert resp.get('email')
        assert isinstance(resp.get('balance_rub'), float)
        assert isinstance(resp.get('balance_usd'), float)
        assert resp.get('email_newsletter')
        assert isinstance(resp.get('hold_balance')["sum_hold_rub"], int)
        assert isinstance(resp.get('hold_balance')["sum_hold_usd"], int)
        assert resp.get('banner') == None

    @allure.title('Test reset password')
    def test_reset_password(self):
        email = TEMP_EMAIL_CREDS["email"]
        password = RegisterUser.random()["password"]
        token_resp = get_tokens(email, password)
        response = User(url=URL).reset_password(body={"email": email}, headers={
            "Authorization": f"Bearer {token_resp['access']}"}, schema=valid_schema)
        messages = RegisterUser.get_messages()
        # if len(messages) > 1:  "Reset password message recieved" # UPDATE CHECK FOR MESSAGE
        # 1 email after registration, 2 email activation letter, 3 email for reseting password
        assert len(messages) == 3
        assert response.status == 204

    @allure.title('Reset password confirm')
    def test_password_confirm(self):
        token_resp = get_tokens()
        uid, token = RegisterUser.get_reset_password_data()
        # # # # # #
        response = User(url=URL).reset_password_confirm(body={"uid": uid, "token": token, "new_password": TEST_PASS}, headers={
            "Authorization": f"Bearer {token_resp['access']}"}, schema=valid_schema)
        assert response.status == 204

    @allure.title('Test change password')
    # NEED TO FIX: ERROR --> {"detail":"TOKEN_NOT_CORRECT"}  NOT IN USE CURRENTLY
    @pytest.mark.skip(reason="Route no in use currently")
    def test_change_password(self):
        tokens_resp = get_tokens()  # GET access/refesh tokens
        uid, token = RegisterUser.get_reset_password_data()
        data = RegisterUser.random()
        current_password = data["password"]
        # # # # # #
        response = User(url=URL).reset_password_confirm(body={"new_password": TEST_PASS, "current_password": current_password, "uid": uid, "token": token}, headers={
            "Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
        assert response.status == 204

    @allure.title('Delete user')
    # NEED TO FIX THIS IN ORDER TO USE FIXTURE FUNCTION WITH PASSING PARAMETERS
    @pytest.mark.skip(reason="Route no in use currently")
    # @pytest.mark.parametrize('get_auth_tokens', ['User1', TEST_PASS])
    def test_delete_user(self):
        data = RegisterUser.random()
        # GET access/refesh tokens for the right user
        tokens_resp = get_tokens(data["email"], TEST_PASS)
        # # # # # #
        response = User(url=URL).delete_user(
            headers={"Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
        assert response.status == 204


@ allure.story('Catalog API')
class TestCatalog:
    @allure.title('Get catalogs')
    # REFACTOR TEST (NEED TO CHECK CORRECT CATALOG)
    def test_get_catalogs(self, get_auth_tokens):
        response = Catalog(url=URL).get_catalogs(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        res = response.response
        catalog = res[0]  # first catalog
        assert response.status == 200
        assert len(res) == 8
        assert catalog.get('id')
        assert catalog.get('title')
        assert catalog.get('code_course')
        assert isinstance(catalog.get('offer'), Iterable)
        assert catalog.get('lending_url') == ""
        assert isinstance(catalog.get('lending_url'), str)
        assert catalog.get('remuneration_percent')
        assert catalog.get('icon')
        assert catalog.get('hold_duration')
        assert catalog.get('canceled_duration')
        assert catalog.get('is_promo')
        assert catalog.get('promo')
        assert catalog.get('category')
        assert catalog.get('approval_rate')
        assert catalog.get('business_partner')
        assert catalog.get('offer_geo')
        assert catalog.get('catalog_id')
        assert catalog.get('preview_image')
        assert catalog.get('company_logo')
        assert catalog.get('description')
        assert catalog.get('reward_type')
        assert catalog.get('devises')
        assert catalog.get('localization')
        assert catalog.get('modified_at')
        assert catalog.get('disable')

    @allure.title('Create catalog')
    def test_create_catalog(self, get_auth_tokens):
        response = Catalog(url=URL).create_catalog(body=CreateCatalog.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        res = response.response
        # created_catalog = res[-1:]  # last catalog
        assert response.status == 201

    @allure.title('Get catalog')
    @pytest.mark.get_partner_catalog
    def test_get_catalog(self, get_auth_tokens):
        response = Catalog(url=URL).get_catalog(uid="5420dbef-423b-4f2c-af1e-b179041ff010", headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        res = response.response
        assert response.status == 200
        assert res.get("id")
        assert res.get("title") == "Test Catalog QA"
        assert res.get("catalog_code") == "test_catalog"

    @allure.title('Update catalog')
    @pytest.mark.skip(reason="Not used in the Frontend/ Used on the Backend - double check")
    def test_update_catalog(self, get_auth_tokens):
        response = Catalog(url=URL).update_catalog(uid="9bce21ea-c8da-43e7-a563-ee05f22c1ed6", body=CreateCatalog.updated_data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        # assert resp.get("code_course") == "test_catalog"
        # assert resp.get("remuneration_percent") == 30
        # assert resp.get("description") == "some_text_new"
        # assert resp.get("lending_url") == "https://example.com/"
        # assert resp.get("hold_duration") == "40 00:00:00"
        # assert resp.get("canceled_duration") == "20 00:00:00"

    @allure.title('Partial update catalog')
    def test_part_update_catalog(self, get_auth_tokens):
        response = Catalog(url=URL).update_catalog(uid="5420dbef-423b-4f2c-af1e-b179041ff010", body=CreateCatalog.part_updated_data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("title") == "SuperCatalogUpdated"
        assert resp.get("catalog_code") == "test_catalog"
        assert resp.get("remuneration_percent") == 25
        assert resp.get("description") == "some_text_new_updated"
        assert resp.get("lending_url") == "https://example.com/test"
        assert resp.get("hold_duration") == "50 00:00:00"
        assert resp.get("canceled_duration") == "30 00:00:00"

    # @allure.title('Add user to catalog')
    # def test_add_user_catalog(self):
    #     # GET NEW USER AND ADD THIS USER TO CATALOG #
    #     # # # Register New user # # #
    #     user_body = RegisterUser.random()
    #     User(url=URL).register_user(body=user_body, schema=valid_schema)
    #     # # #  Activate # # #
    #     uid, token = RegisterUser.get_activation_data()
    #     body = {'uid': uid, 'token': token}
    #     User(url=URL).activate_user(body=body, schema=valid_schema)

    #     # # GET access/refesh tokens for created user
    #     tokens_resp = get_auth_tokens(
    #         user_body["email"], user_body["password"])
    #     id = "e03713b3-727c-4b38-ac92-072550d78163"  # TestCatalog
    #     # # # # # #
    #     response = Catalog(url=URL).add_user_catalog(uid=id, headers={
    #         "Authorization": f"Bearer {tokens_resp['access']}"}, schema=valid_schema)
    #     resp = response.response
    #     assert response.status == 200
    #     assert resp == {"detail": "USER_ADDED"}

    @allure.title('Set taffic rule for catalog')
    @pytest.mark.set_rule_traffic
    def test_set_rule_traffic(self, get_auth_tokens):
        response = Catalog(url=URL).set_rule_traffic(uid="5420dbef-423b-4f2c-af1e-b179041ff010", body=CreateCatalog.set_rule_data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        for key in CreateCatalog.set_rule_data:
            assert resp.get(key)

    @allure.title('Get catalog by catalog code')
    @pytest.mark.get_catalog_by_code
    def test_catalog_by_code(self, get_auth_tokens):
        response = Catalog(url=URL).get_catalog_by_code(catalog_code="test_catalog", headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @allure.title('Get catalog by user')
    def test_catalog_by_user(self, get_auth_tokens):
        response = Catalog(url=URL).get_catalog_by_user(
            headers={"Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @allure.title('Get catalog with deals')
    def test_catalog_with_deals(self, get_auth_tokens):
        response = Catalog(url=URL).get_catalog_with_deals(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @allure.title('Get offer contains deals by catalog')
    @pytest.mark.offer_with_deals
    # ADD DEALS FOR USER
    def test_offer_with_deals(self, get_auth_tokens):
        response = Catalog(url=URL).get_offer_with_deals(catalogs="9bce21ea-c8da-43e7-a563-ee05f22c1ed6", headers={"Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200


@ allure.story('Offer API')
class TestOffer:
    @allure.title('Get offer')
    @pytest.mark.create_offer
    def test_create_offer(self, get_auth_tokens):
        response = Offer(url=URL).create_offer(body=OfferData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("name")
        assert resp.get("catalog_id")
        assert resp.get("is_promocode_allowed") == False
        assert resp.get("is_active")
        assert resp.get("prices")
        assert isinstance(resp.get("prices")[0], dict)
        assert resp.get("description")
        assert resp.get("reward_percent") == None
        assert resp.get("fix_remuneration") == 4
        #
        OfferValueStorage.id = resp.get("id")

    @pytest.mark.get_offer
    def test_get_offer(self, get_auth_tokens):
        response = Offer(url=URL).get_offer(id=OfferValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")

    @pytest.mark.update_offer
    def test_update_offer(self, get_auth_tokens):
        response = Offer(url=URL).update_offer(body=OfferData.data_updated, id=OfferValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("name") == OfferData.data_updated["name"]
        assert resp.get("is_promocode_allowed") == OfferData.data_updated["is_promocode_allowed"]
        assert resp.get("is_active") == OfferData.data_updated["is_active"]
        assert resp.get("prices")[0]["cost"] == OfferData.data_updated["prices"][0]["cost"]
        assert resp.get("prices")[0]["currency"] == OfferData.data_updated["prices"][0]["currency"]
        assert resp.get("description") == OfferData.data_updated["description"]
        assert resp.get("fix_remuneration") == OfferData.data_updated["fix_remuneration"]

    @pytest.mark.part_upd_offer
    def test_part_upd_offer(self, get_auth_tokens):
        response = Offer(url=URL).part_update_offer(body=OfferData.part_data_updated, id=OfferValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("prices")[1]["cost"] == OfferData.part_data_updated["prices"][1]["cost"]
        assert resp.get("prices")[1]["currency"] == OfferData.part_data_updated["prices"][1]["currency"]


@allure.story('Deals API')
class TestDeals:
    # PASS ONLY PAGE-SIZE parameter to check route
    @pytest.mark.get_deals
    def test_get_deals(self, get_auth_tokens):
        response = Deals(url=URL).get_deals(parameter="page", value="1", headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.create_deal
    def test_create_deal(self, get_auth_tokens):
        response = Deals(url=URL).create_deal(body=DealData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("status")
        assert resp.get("offer")
        assert resp.get("cost")
        assert resp.get("currency")
        assert resp.get("deal_id")
        assert resp.get("promo_code")
        assert resp.get("catalog_code")
        assert resp.get("another_data")
        assert resp.get("is_returned")

    @pytest.mark.get_deal
    def test_get_deal(self):
        response = Deals(url=URL).get_deal(id="test_deal_id", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("status")

    @pytest.mark.update_deal
    def test_update_deal(self):
        response = Deals(url=URL).update_deal(body=DealData.data_updated, id="Deal_for_Test", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("status")

    @pytest.mark.get_count_deals
    def test_count_deals(self, get_auth_tokens):
        response = Deals(url=URL).get_count_deals(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert isinstance(resp.get("offer"), dict)
        assert isinstance(resp.get("currency"), dict)
        assert isinstance(resp.get("status"), dict)
        assert isinstance(resp.get("promo"), dict)

    # CHECK HOW IT WORKS AND IT's PARAMETERS
    @pytest.mark.gen_stat_deals
    def test_gen_stat_deals(self, get_auth_tokens):
        response = Deals(url=URL).gen_stat_deals(params=None, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("count")
        assert resp.get("next")
        assert resp.get("previous") == None
        assert isinstance(resp.get("results"), Iterable)
        assert len(resp.get("results")) == 10
        assert isinstance(resp.get("sum_by_status"), dict)

    # CHECK HOW IT WORKS AND IT's PARAMETERS
    @pytest.mark.get_stat_user_deals
    def test_stat_user_deals(self, get_auth_tokens):
        response = Deals(url=URL).get_stat_user_deals(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    # WHAT PARAMS ARE USED AND HOW TO CHECK THEM PROPERLY
    @pytest.mark.get_params_deals
    def test_params_deals(self, get_auth_tokens):
        response = Deals(url=URL).get_params_deals(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.get_stat_deals
    def test_stat_deals(self, get_auth_tokens):
        response = Deals(url=URL).get_stat_deals(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert isinstance(resp.get("deal_paid"), int)
        assert isinstance(resp.get("deal_approved"), int)
        assert isinstance(resp.get("deal_canceled"), int)
        assert isinstance(resp.get("deal_rejected"), int)
        assert resp.get("sum_deal_paid") == None
        assert resp.get("sum_deal_approved") == None
        assert resp.get("sum_deal_canceled") == None
        assert resp.get("sum_deal_created") == None
        assert resp.get("sum_deal_rejected")


@allure.story('Landning API')
class TestLanding:
    @pytest.mark.create_landing
    def test_create_landing(self, get_auth_tokens):
        response = Landing(url=URL).create_landing(body=LandingData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("modified_at")
        assert resp.get("url") == LandingData.data["url"]
        assert resp.get("adaptability") == LandingData.data["adaptability"]
        assert resp.get("title") == LandingData.data["title"]
        assert resp.get("catalog_id") == LandingData.data["catalog_id"]
        assert resp.get("image_url")
        #
        LandingValueStorage.id = resp.get("id")

    @pytest.mark.update_landing
    def test_update_landing(self, get_auth_tokens):
        response = Landing(url=URL).update_landing(body=LandingData.data_updated, id=LandingValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("modified_at")
        assert resp.get("url") == LandingData.data_updated["url"]
        assert resp.get("adaptability") == LandingData.data_updated["adaptability"]
        assert resp.get("title") == LandingData.data_updated["title"]
        assert resp.get("catalog_id") == LandingData.data_updated["catalog_id"]
        assert resp.get("image_url")

    @pytest.mark.part_upd_landing
    def test_part_upd_landing(self, get_auth_tokens):
        response = Landing(url=URL).part_upd_landing(body=LandingData.data_part_updated, id=LandingValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("adaptability") == LandingData.data_part_updated["adaptability"]

    @pytest.mark.delete_landing
    def test_delete_landing(self, get_auth_tokens):
        response = Landing(url=URL).delete_landing(id=LandingValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 204


@allure.story('Personal Domain API')
class TestDomain:
    @pytest.mark.get_domains
    def test_get_domains(self):
        response = PersonalDomain(url=URL).get_domains(
            headers={"Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("domain")

    @pytest.mark.create_domain
    def test_create_domain(self):
        response = PersonalDomain(url=URL).create_domain(body=DomainData.data, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("domain")
        #
        DomainValueStorage.id = resp.get("id")

    @pytest.mark.get_domain
    def test_get_domain(self):
        response = PersonalDomain(url=URL).get_domain(id=DomainValueStorage.id, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("domain") == DomainData.data["domain"]

    @pytest.mark.update_domain
    def test_update_domain(self):
        response = PersonalDomain(url=URL).update_domain(body=DomainData.data_updated, id=DomainValueStorage.id, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("domain") == DomainData.data_updated["domain"]

    @pytest.mark.part_upd_domain
    def test_part_upd_domain(self):
        response = PersonalDomain(url=URL).part_upd_domain(body=DomainData.part_data_updated, id=DomainValueStorage.id, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("domain") == DomainData.part_data_updated["domain"]

    @pytest.mark.delete_domain
    def test_delete_domain(self):
        response = PersonalDomain(url=URL).delete_domain(id=DomainValueStorage.id, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 204


@allure.story('Promo')
class TestPromo:
    name = 'Promo_' + "".join(random.choice(string.ascii_letters)
                              for i in range(10))

    @pytest.mark.create_promo
    def test_create_promo(self, get_auth_tokens, get_catalog_id):
        # Get catalog id just one time and save to variable to use inside the class!
        CatalogIdValueStorage.id = get_catalog_id
        data = {
            "code": self.name,
            "percent_discounts": 8,
            "catalog": [
                CatalogIdValueStorage.id
            ]
        }
        response = Promo(url=URL).create_promo(body=data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("code") == self.name
        assert resp.get("percent_discounts") == 8.0
        assert resp.get("catalog")
        #
        PromoValueStorage.id = resp.get("id")

    @pytest.mark.get_promo
    def test_get_promo(self, get_auth_tokens):
        response = Promo(url=URL).get_promo(id=PromoValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")

    @pytest.mark.update_promo
    def test_update_promo(self, get_auth_tokens):
        data_updated = {
            "code": self.name + "Updated",
            "percent_discounts": 9,
            "catalog": [
                CatalogIdValueStorage.id
            ]
        }
        response = Promo(url=URL).update_promo(body=data_updated, id=PromoValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("code") == self.name + "Updated"
        assert resp.get("percent_discounts") == 9.0
        assert resp.get("catalog")

    @pytest.mark.part_upd_promo
    def test_part_upd_promo(self, get_auth_tokens):
        part_data_updated = {"percent_discounts": 7}

        response = Promo(url=URL).part_upd_promo(body=part_data_updated, id=PromoValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("percent_discounts") == 7.0

    # SHOULD BE IN THE SAME CATALOG
    @pytest.mark.check_promo
    def test_check_promo(self):
        response = Promo(url=URL).check_promo(catalog_id="U32FA", code="1E68HXM5LQ02", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    # ADD ASSERTIONS
    @pytest.mark.check_promo_bycode
    def test_check_promo_bycode(self):
        response = Promo(url=URL).check_promo_bycode(catalog_code="test_catalog", code="1E68HXM5LQ02", headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    # PASS User ID as a parameter
    @pytest.mark.check_uuid
    def test_check_uuid(self):
        response = Promo(url=URL).check_uuid(user_id='UFGSX3JM', headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.check_promo_user
    @pytest.mark.skip(reason="WAITING FOR FIX")
    def test_user_promo(self):
        response = Promo(url=URL).create_promo_user(body=PromoData.bp_promo_data, headers={
            "Authorization": AUTH_TOKEN}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.check_promo_prefix
    @pytest.mark.skip(reason="NOT USED, WATING FOR THE BUSINESS LOGIC")
    def test_promo_prefix(self, get_auth_tokens):
        response = Promo(url=URL).create_promo_prefix(body={"prefix_promo_code": "TEST_PREFIX"}, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("prefix_promo_code") == "TEST_PREFIX"


@allure.story('Promo Material')
class TestMaterial:
    @pytest.mark.create_material
    def test_create_material(self, get_auth_tokens):
        response = PromoMaterial(url=URL).create_material(body=MaterialData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("url") == MaterialData.data["url"]
        assert resp.get("type_material") == MaterialData.data["type_material"]
        assert resp.get("catalog") == MaterialData.data["catalog"]
        assert resp.get("title") == MaterialData.data["title"]
        #
        MaterialValueStorage.id = resp.get("id")

    @pytest.mark.get_material
    def test_get_material(self, get_auth_tokens):
        response = PromoMaterial(url=URL).get_material(id=MaterialValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("url")
        assert resp.get("type_material")
        assert resp.get("catalog")
        assert resp.get("title")

    @pytest.mark.update_material
    def test_update_material(self, get_auth_tokens):
        response = PromoMaterial(url=URL).update_material(body=MaterialData.data_updated, id=MaterialValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("url") == MaterialData.data_updated["url"]
        assert resp.get("type_material") == MaterialData.data_updated["type_material"]
        assert resp.get("catalog") == MaterialData.data_updated["catalog"]
        assert resp.get("title") == MaterialData.data_updated["title"]

    @pytest.mark.part_upd_material
    def test_part_upd_material(self, get_auth_tokens):
        response = PromoMaterial(url=URL).part_upd_material(body=MaterialData.part_data_updated, id=MaterialValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("type_material") == MaterialData.part_data_updated["type_material"]


@allure.story('Text Rule')
class TestTextRule:
    name = 'Rule_' + "".join(random.choice(string.ascii_letters)
                             for i in range(10))

    @pytest.mark.create_text_rule
    def test_create_rule(self, get_auth_tokens):
        data = {
            "text": self.name,
            "language": "RU",
            "catalog": CatalogIdValueStorage.id  # Use newely created catalog
        }

        response = TextRule(url=URL).create_rule(body=data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("text") == data["text"]
        assert resp.get("language") == data["language"]
        assert resp.get("catalog") == data["catalog"]
        #
        TextRuleValueStorage.id = resp.get("id")

    @pytest.mark.get_text_rule
    def test_get_text_rule(self, get_auth_tokens):
        response = TextRule(url=URL).get_rule(id=TextRuleValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")

    @pytest.mark.update_text_rule
    def test_update_text_rule(self, get_auth_tokens):

        data_updated = {
            "text": self.name + "Updated",
            "language": "EN",
            "catalog": CatalogIdValueStorage.id
        }
        response = TextRule(url=URL).update_rule(body=data_updated, id=TextRuleValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("text") == data_updated["text"]
        assert resp.get("language") == data_updated["language"]
        assert resp.get("catalog") == data_updated["catalog"]

    @pytest.mark.part_upd_text_rule
    def test_part_upd_text_rule(self, get_auth_tokens):
        response = TextRule(url=URL).part_upd_rule(body=TextRuleData.part_data_updated, id=TextRuleValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("language") == TextRuleData.part_data_updated["language"]

    @pytest.mark.delete_text_rule
    def test_delete_text_rule(self, get_auth_tokens):
        response = TextRule(url=URL).delete_rule(id=TextRuleValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        assert response.status == 204

    @pytest.mark.get_rule_catalog
    def test_get_rule_catalog(self, get_auth_tokens):
        response = TextRule(url=URL).get_rule_catalog(catalog_id="5420dbef-423b-4f2c-af1e-b179041ff010", headers={"Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200


@allure.story('Ads Template')
class TestAdsTemplate:
    @pytest.mark.get_all_templates
    def test_get_all_templates(self, get_auth_tokens):
        response = AdsTemplate(url=URL).get_templates(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert isinstance(resp, Iterable)

    @pytest.mark.get_template
    def test_get_template(self, get_auth_tokens):
        response = AdsTemplate(url=URL).get_template(id="UZH0LV", headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("name")


@allure.story('Link Constructor')
class TestLinkConstructor:
    @pytest.mark.create_link_constructor
    def test_create_link_constructor(self, get_auth_tokens):
        response = LinkConstructor(url=URL).create_link_constructor(body=LinkConstructorData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("domain") == LinkConstructorData.data["domain"]
        assert resp.get("landing") == LinkConstructorData.data["landing"]
        assert resp.get("ads_template") == LinkConstructorData.data["ads_template"]
        assert resp.get("modified_at")
        assert resp.get("url")
        assert resp.get("parking_url")
        #
        LinkConstValueStorage.id = resp.get("id")

    @pytest.mark.update_link_constructor
    def test_update_link_constructor(self, get_auth_tokens):
        response = LinkConstructor(url=URL).update_link_constructor(body=LinkConstructorData.data_updated, id=LinkConstValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("domain") == LinkConstructorData.data_updated["domain"]
        assert resp.get("landing") == LinkConstructorData.data_updated["landing"]
        assert resp.get("ads_template") == LinkConstructorData.data_updated["ads_template"]

    @pytest.mark.part_upd_link_constructor
    def test_part_upd_link_constructor(self, get_auth_tokens):
        response = LinkConstructor(url=URL).part_upd_link_constructor(body=LinkConstructorData.part_data_updated, id=LinkConstValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("subid") == LinkConstructorData.part_data_updated["subid"]

    @pytest.mark.delete_link_constructor
    def test_delete_link_constructor(self, get_auth_tokens):
        response = LinkConstructor(url=URL).delete_link_constructor(id=LinkConstValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        assert response.status == 204


@allure.story('Postback')
class TestPostback:
    @pytest.mark.get_postback_list
    def test_get_postback_list(self, get_auth_tokens):
        response = Postback(url=URL).get_postback_list(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("count")
        assert isinstance(resp.get("results"), Iterable)

    @pytest.mark.create_postback
    def test_create_postback(self, get_auth_tokens):
        response = Postback(url=URL).create_postback(body=PostbackData.data, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 201
        assert resp.get("id")
        assert resp.get("url") == PostbackData.data["url"]
        assert resp.get("user_url") == PostbackData.data["user_url"]
        assert resp.get("status") == PostbackData.data["status"]
        assert resp.get("user") == "UFGSX3JM"
        assert len(resp.get("postback_field")) == len(PostbackData.data["postback_field"])
        assert resp.get("catalog")[0] == PostbackData.data["catalog"]
        assert resp.get("postback_template") == PostbackData.data["postback_template"]
        #
        PostbackValueStorage.id = resp.get("id")

    @pytest.mark.get_postback
    def test_get_postback(self, get_auth_tokens):
        response = Postback(url=URL).get_postback(id=PostbackValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")

    @pytest.mark.update_postback
    def test_update_postback(self, get_auth_tokens):
        response = Postback(url=URL).update_postback(body=PostbackData.data_updated, id=PostbackValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert resp.get("id")
        assert resp.get("url") == PostbackData.data_updated["url"]
        assert resp.get("user_url") == PostbackData.data_updated["user_url"]
        assert resp.get("status") == PostbackData.data_updated["status"]
        assert resp.get("user") == "UFGSX3JM"
        assert len(resp.get("postback_field")) == len(PostbackData.data_updated["postback_field"])
        assert resp.get("catalog")[0] == PostbackData.data_updated["catalog"]
        assert resp.get("postback_template") == PostbackData.data_updated["postback_template"]

    @pytest.mark.delete_postback
    def test_delete_postback(self, get_auth_tokens):
        response = Postback(url=URL).delete_postback(id=PostbackValueStorage.id, headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        assert response.status == 204

    @pytest.mark.get_postback_templates
    def test_postback_templates(self, get_auth_tokens):
        response = Postback(url=URL).get_postback_templates(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert isinstance(resp, Iterable)

    @pytest.mark.check_postback_url
    @pytest.mark.skip(reason="Doesn't have response body!")
    def test_postback_url(self, get_auth_tokens):
        response = Postback(url=URL).check_postback_url(url="https://example.com/", headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200

    @pytest.mark.check_postback_field_enum
    def test_postback_field_enum(self, get_auth_tokens):
        response = Postback(url=URL).postback_field_enum(headers={
            "Authorization": f"Bearer {get_auth_tokens['access']}"}, schema=valid_schema)
        resp = response.response
        assert response.status == 200
        assert isinstance(resp, Iterable)
