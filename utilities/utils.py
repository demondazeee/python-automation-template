import softest


class Utils(softest.TestCase):

    def assertText(self, actual_text: str, expected_text: str):
        self.soft_assert(self.assertEqual, actual_text, expected_text)

        self.assert_all()

    def assertIn(self, actual_text: str, expected_text: str):
        self.soft_assert(self.assertTrue, expected_text in actual_text)

        self.assert_all()
