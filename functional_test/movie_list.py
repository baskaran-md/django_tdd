__author__ = 'baskar'

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EndUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("localhost:8000")
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_add_a_movie_and_fetch_it(self):
        import time
        time.sleep(3)

        # Test the Title
        self.assertEqual("Movie List",self.browser.title)

        # Test the Header
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("My Movie List", header_text)

        # Check the input text box
        input_box = self.browser.find_element_by_id("id_movie_name")
        input_box_place_holder = input_box.get_attribute("placeholder")
        self.assertEqual(input_box_place_holder, "Enter a Movie Name")

        # Add a movie name in the input text box
        input_box.send_keys("Frozon")
        input_box.send_keys(Keys.ENTER)

        # Check the text box is empty after adding
        #input_box_place_holder = input_box.get_attribute("placeholder")
        #self.assertEqual(input_box_place_holder,"Enter a Movie Name")

        # Check the movie name in movie list table
        table = self.browser.find_element_by_id("id_movie_list_table")
        table_rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(any("Frozon" in row.text for row in table_rows), "Movie Frozon is not in the table")



if __name__ == 'main':
    unittest.main()