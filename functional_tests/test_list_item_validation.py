from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
import time

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # she sends an empty to-do item
        # press enter without any input in the input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # the page refreshes and sends a error message
        # "the to-do item can not be empty"
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        )
        )
        # she enters something and submit, done!
        self.fail("finish this test!")
        # she sends another empty to-do item

        # on the list page, she get the error message again

        # she enters something again and done!
        self.fail('write me!')