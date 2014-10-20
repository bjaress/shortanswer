from hamcrest import *
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as condition
from selenium.webdriver.support.ui import WebDriverWait

from django.test import TestCase
from functional_tests import SERVER_URL


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

        self.browser.get(SERVER_URL+"/question")
        submit_button = self.browser.find_element_by_css_selector("input[type=submit]")
        question_input = self.browser.find_element_by_tag_name("textarea")
        question_input.send_keys(LONG_QUESTION)
        submit_button.click()

        WebDriverWait(self.browser, 10).until(
                condition.visibility_of_element_located(
                    (By.CLASS_NAME, "question")))
        displayed_question = self.browser.find_element_by_class_name("question")
        assert_that(displayed_question.text, equal_to(LONG_QUESTION),
                "Questions should be shown after they are submitted")


LONG_QUESTION = """Centuries ago there lived--

"A king!" my little readers will say immediately.

No, children, you are mistaken. Once upon a time there was a piece of
wood. It was not an expensive piece of wood. Far from it. Just a common
block of firewood, one of those thick, solid logs that are put on the
fire in winter to make cold rooms cozy and warm.

I do not know how this really happened, yet the fact remains that one
fine day this piece of wood found itself in the shop of an old
carpenter. His real name was Mastro Antonio, but everyone called him
Mastro Cherry, for the tip of his nose was so round and red and shiny
that it looked like a ripe cherry.
"""


if __name__ == '__main__':
    unittest.main()
