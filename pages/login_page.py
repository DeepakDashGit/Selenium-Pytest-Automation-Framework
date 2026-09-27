from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    REQUIRED_MESSAGE = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_required_message(self):
        return self.get_text(self.REQUIRED_MESSAGE)