from selenium import webdriver
import unittest
from urllib import request

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
        compressed = [element.get_attribute('src')
                for element in self.browser.find_elements_by_tag_name('script')
                if 'CACHE' in element.get_attribute('src')]
        self.assertTrue(len(compressed) > 0,
                msg="At least some scripts should be compressed.")
        for url in compressed:
            self.follow(url)

    def test_styles(self):
        """Check that the style-sheets are hooked up and the compressor
        isn't choking.

        """
        self.browser.get(SERVER)
        compressed = [element.get_attribute('href')
                for element in self.browser.find_elements_by_tag_name('link')
                if element.get_attribute('rel') == 'stylesheet'
                    and 'CACHE' in element.get_attribute('href')]
        self.assertTrue(len(compressed) > 0,
                msg="At least some style-sheets should be compressed.")
        for url in compressed:
            self.follow(url)

    def follow(self, url):
        self.browser.get(url)
        result = request.urlopen(url)
        self.assertTrue(len(result.read()) > 0,
                msg="URL should lead somewhere.")
        return True

if __name__ == '__main__':
    unittest.main()
