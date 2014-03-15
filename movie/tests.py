from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.template.loader import render_to_string

from .views import home_page


class HomePageTest(TestCase):

    def test_home_page_url_resolve(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_html_content(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith("<html>"))
        self.assertTrue(response.content.endswith("</html>"))
        self.assertIn("<title>Movie List</title>", response.content)
        self.assertIn("<h1>My Movie List</h1>", response.content)