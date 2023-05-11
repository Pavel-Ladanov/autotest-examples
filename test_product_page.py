from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.sleep(2)

def test_valid_product_name_in_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.sleep(2)
