from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import home_page

class DemoTest(TestCase):

    def test_add(self):
        self.assertEqual(10 + 10, 20)

    def test_subtract(self):
        self.assertEqual(10 - 10, 0)

    def test_multiply(self):
        self.assertEqual(10 * 10, 100)


class HomePageTest(TestCase):

    def test_home_page_url_resolve(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)
