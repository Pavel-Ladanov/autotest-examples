from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators ():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_ADD_TO_CART_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
