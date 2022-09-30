from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_presence_of_element(self, locator_type, locator: str):
        element = self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements(self, locator_type, locator: str):
        elements = self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return elements

    def text_element(self, locator_type, locator, text):
        result = self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))
        return result

    def close_current_window(self):
        self.driver.close()