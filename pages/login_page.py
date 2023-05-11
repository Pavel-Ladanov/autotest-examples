from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):

    def should_be_login_page(self):
        assert 'login' in self.browser.current_url, 'wrong url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no registration form"