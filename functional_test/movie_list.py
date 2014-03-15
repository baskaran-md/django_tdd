__author__ = 'baskar'

from selenium import webdriver
import unittest

class EndUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("localhost:8000")

    def tearDown(self):
        self.browser.quit()

    def test_add_a_movie_and_fetch_it(self):
        self.assertIn('Movie', self.browser.title)


if __name__ == 'main':
    unittest.main()