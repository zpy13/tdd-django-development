from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def tearDown(self):
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test!')

	# the app invited her to enter a to-do item

	# she entered 'Buy percock feathers' in a text box

	# she pressed the enter button and the page got updated
	# '1: Buy peacock feathers'

if __name__ == '__main__':
	#unittest.main(warnings='ignore')
	unittest.main()
