from base.base_driver import BaseDriver
from .secure_area_page import SecureAreaPage
from selenium.webdriver.common.by import By


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="radius"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@class="flash error"]')

    def __get_username(self):
        return self.wait_for_presence_of_element(*self.USERNAME_FIELD)

    def __get_password(self):
        return self.wait_for_presence_of_element(*self.PASSWORD_FIELD)

    def __get_login_button(self):
        return self.wait_for_presence_of_element(*self.LOGIN_BUTTON)

    def __get_error_message(self):
        return self.wait_for_presence_of_element(*self.ERROR_MESSAGE)


    # ACTIONS

    def navigate(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def input_username(self, username: str):
        self.__get_username().send_keys(username)

    def input_password(self, password: str):
        self.__get_password().send_keys(password)

    def get_error_message_text(self):
        return self.__get_error_message().text

    def click_login(self):
        self.__get_login_button().click()
        secure_area_page = SecureAreaPage(self.driver)
        return secure_area_page
