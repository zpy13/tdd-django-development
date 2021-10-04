from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # she sends an empty to-do item
        # press enter without any input in the input box

        # the page refreshes and sends a error message
        # "the to-do item can not be empty"

        # she enters something and submit, done!

        # she sends another empty to-do item

        # on the list page, she get the error message again

        # she enters something again and done!
        self.fail('write me!')
