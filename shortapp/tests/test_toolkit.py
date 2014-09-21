from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from ..views import home_page

class ToolkitTest(TestCase):
    """Test the loading of basic tools."""

    def test_root(self):
        """Quick check that we can actually load the homepage."""
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_jquery_mobile(self):
        """We're using jQuery Mobile as a client-side interface tool, on
        both mobile and desktop.

        """

        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'/jquerymobile/', response.content)
        self.assertIn(b'/jquery/', response.content)
