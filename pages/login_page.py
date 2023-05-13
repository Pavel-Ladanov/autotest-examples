from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        assert 'login' in self.browser.current_url, 'wrong url'
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no login form"
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no registration form"
    def register_new_user(self, email, password='10203456789'):
        self.send_text_to_element(*LoginPageLocators.EMAIL_REGISTRATION_FIELD, email)
        self.send_text_to_element(*LoginPageLocators.PASSWORD1_REGISTRATION_FIELD, password)
        self.send_text_to_element(*LoginPageLocators.PASSWORD2_REGISTRATION_FIELD, password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_button.click()
        assert self.element_text(*LoginPageLocators.SUCCESS_REGISTRATION_MESSAGE)== 'Спасибо за регистрацию!',"cant registration"