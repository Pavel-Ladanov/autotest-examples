import pytest
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
list_of_failed_num = [7]
tested_links = [f"{product_base_link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{product_base_link}?promo=offer{i}",
                             marks=pytest.mark.skip)for i in range(10)]

@pytest.mark.parametrize('link', tested_links)
class TestGuestAddPromoProduct:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
    def test_guest_can_see_cart_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_cart_message()
    def test_valid_product_name_in_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_right_product_name()
    def test_valid_product_price_in_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_cart_message()
        page.should_be_right_product_price()
class TestGuestCanGoToLoginPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page (self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        backet_page = BasketPage(browser, browser.current_url)
        backet_page.should_be_no_items_in_basket()
    @pytest.mark.xfail(reason="that's how it should be")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,link)
        page.open()
        page.product_add_to_cart()
        page.should_not_be_success_message()
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    @pytest.mark.xfail(reason="that's how it should be")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.should_be_disappeared_success_message()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org")
        page.should_be_authorized_user()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.product_add_to_cart()
        page.should_be_success_message()
    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()