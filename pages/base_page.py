from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import MainPageLocators
import time
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    def go_to_login_page(self):
        try:
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        except:
            link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except:
            pass
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_login_link(self):
        try:
            assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        except:
            assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def element_text(self, how, what):
        try:
            text = self.browser.find_element(how, what).text
        except (NoSuchElementException):
            return False
        return str(text)
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
    def send_text_to_element(self, how, what,text):
        try:
            element = self.browser.find_element(how, what)
            element.send_keys(text)
        except (NoSuchElementException):
            return False
    def sleep(self,sec):
        time.sleep(sec)