__author__ = 'baskar'

import unittest
import time


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
        time.sleep(1)

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
        self.add_content_in_movie_name_input_box("Troy")
        self.check_content_in_movie_list_table("Troy")

        self.add_content_in_movie_name_input_box("Frozon")
        self.check_content_in_movie_list_table("Frozon")

    def add_content_in_movie_name_input_box(self, movie_name):
        input_box = self.browser.find_element_by_id("id_movie_name")
        input_box.send_keys(movie_name)
        input_box.send_keys(Keys.ENTER)

    def check_content_in_movie_list_table(self, movie_name):
        table = self.browser.find_element_by_id("id_movie_list_table")
        table_rows = table.find_elements_by_tag_name("tr")
        time.sleep(2)
        self.assertTrue(any(movie_name in table_row.text for table_row in table_rows),
                        "Movie %s is not added to the table. Table content: %s" % (movie_name, table.text))


if __name__ == 'main':
    unittest.main()