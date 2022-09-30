import pytest
import softest
from pages.form_authentication.login_page import LoginPage
from ddt import ddt, data, unpack, file_data
from utilities.utils import Utils
from testdata.data import TestData


@pytest.mark.usefixtures('setup')
@ddt
class Test(softest.TestCase):

    # @file_data(TestData.test_data)
    # def test_login(self, username, password, alert_text):
    #     lp = LoginPage(self.driver)

    #     lp.navigate()

    #     lp.input_username(username)

    #     lp.input_password(password)

    #     secure_area = lp.click_login()
    #     alert_message = secure_area.get_alert_message_text()

    #     u = Utils()
    #     u.assertIn(actual_text=alert_message, expected_text=alert_text)

    @file_data(TestData.test_data_invalid)
    def test_login_negative(self, username, password, error_message):
        lp = LoginPage(self.driver)

        lp.navigate()

        lp.input_username(username)

        lp.input_password(password)

        lp.click_login()

        lp.close_current_window()
        # error_message_text = lp.get_error_message_text()

        # u = Utils()
        # a = u.verify_error_messages(self.driver, ['Login Page'])
        # print(a)
        # u.assertIn(actual_text=error_message_text, expected_text=error_message)
