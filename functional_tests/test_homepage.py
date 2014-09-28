from selenium import webdriver
import unittest
from django.test import TestCase

SERVER='http://localhost:5000'

class BasicLinksTest(TestCase):
    """Check that the main links are on the homepage."""

    def setUp(self):
        """Selenium browser."""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Cleanup browser."""
        self.browser.quit()

    def test_source_link(self):
        """Checks for a source link.

        This won't check that the link actually points to the correct
        version and fork of the source, just that a link is there.

        """
        self.browser.get(SERVER)
        source_link = self.browser.find_element_by_id('sourceLink')
        self.assertEqual("source code", source_link.text,
                msg="Homepage should link to source code.")
        self.assertTrue("://" in source_link.get_attribute('href'),
                msg="Source code link should reference something.")

if __name__ == '__main__':
    unittest.main()
