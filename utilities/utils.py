import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Utils(softest.TestCase):

    def verify_error_messages(self, driver, error_messages):
        wait = WebDriverWait(driver, 10)
        isPassed = True
        for message in error_messages:
            # List<WebElement> list = ECDriver.findElements(By.xpath("//*[contains(text(),'" + message + "')]"));
            try:
                list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, f'//*[contains(text(),"{message}")]')))
                if len(list) > 0:
                    isPassed = False
                    break
            except TimeoutException:
                pass
        
        return isPassed

    def assertText(self, actual_text: str, expected_text: str):
        self.soft_assert(self.assertEqual, actual_text, expected_text)

        self.assert_all()

    def assertIn(self, actual_text: str, expected_text: str):
        self.soft_assert(self.assertTrue, expected_text in actual_text)

        self.assert_all()

    def assert_True(self, condition):
        self.assertTrue(condition, 'Error Message found')