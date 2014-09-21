from selenium import webdriver
import unittest

SERVER='http://localhost:5000'

class ToolIntegrationTest(unittest.TestCase):
    """Example test, checking for for tool integration."""

    def setUp(self):
        """Selenium browser."""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """Cleanup browser."""
        self.browser.quit()

    def test_jquery_mobile(self):
        """jQuery mobile jquerymobile.com/"""
        self.browser.get(SERVER)
        scripts = self.browser.find_elements_by_tag_name('script')
        self.assertTrue(
            any('jquery.mobile' in script.get_attribute('src')
                for script in scripts),
            msg="jQuery Mobile should be the default client-side toolkit.")

    def test_scripts(self):
        """Check that the scripts are hooked up and the compressor isn't
        choking.

        """
        self.browser.get(SERVER)
        scripts = self.browser.find_elements_by_tag_name('script')

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Scripts working', header_text)

if __name__ == '__main__':
    unittest.main()
