from selenium import webdriver
import unittest
from django.test import TestCase

SERVER='http://localhost:5000'

class AskQuestion(TestCase):
    """Users can ask questions."""

    def setUp(self):
        """Selenium browser."""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Cleanup browser."""
        self.browser.quit()

    def test_typical_question(self):
        """When the user does it right, it should work."""

        self.browser.get(SERVER+"/question")
        submit_button = self.browser.find_element_by_css_selector("input[type=submit]")
        question_input = self.browser.find_element_by_tag_name("textarea")

if __name__ == '__main__':
    unittest.main()
