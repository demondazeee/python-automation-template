from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By


class SecureAreaPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    ALERT_MESSAGE = (By.XPATH, '//div[@class="flash success"]')

    def __get_alert_message(self):
        return self.wait_for_presence_of_element(*self.ALERT_MESSAGE)

    # ACTIONS

    def get_alert_message_text(self):
        return self.__get_alert_message().text

