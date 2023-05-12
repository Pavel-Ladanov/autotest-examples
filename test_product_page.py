import pytest

from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


list_of_failed_num = [7]
tested_links = [f"{product_base_link}?promo=offer{i}" if i not in list_of_failed_num else
                pytest.param(f"{product_base_link}?promo=offer{i}",
                             marks=pytest.mark.xfail(reason="some bug", strict=True)
                             )for i in range(10)]

@pytest.mark.parametrize('link', tested_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()

@pytest.mark.parametrize('link', tested_links)
def test_guest_can_see_cart_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_cart_message()
@pytest.mark.parametrize('link', tested_links)
def test_valid_product_name_in_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_right_product_name()
@pytest.mark.parametrize('link', tested_links)
def test_valid_product_price_in_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_cart_message()
    page.should_be_right_product_price()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
