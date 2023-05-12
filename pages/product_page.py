from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_CART_MESSAGE), "Success message is not presented"
    def should_be_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_CART_PRICE_MESSAGE), "Success message is not presented"
    def should_be_right_product_price(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_PRICE) ==\
               self.element_text(*ProductPageLocators.PRODUCT_PRICE_IN_CART_PRICE_MESSAGE), "Product price do not match"
    def should_be_right_product_name(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_NAME) ==\
               self.element_text(*ProductPageLocators.SUCCESS_ADD_TO_CART_MESSAGE), "Product name do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared (*ProductPageLocators.SUCCESS_ADD_TO_CART_MESSAGE), \
            "Success message is not disappeared"

