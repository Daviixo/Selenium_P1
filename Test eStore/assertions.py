import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AssertionsTest(unittest.TestCase):

	@classmethod
	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")

	def test_search_field(self):
		print('Searching the search bar')
		self.assertTrue(self.is_element_present(By.NAME, 'q'))

	
	def test_language_option(self):
		print('Searching the Select language dropdown')
		self.assertTrue(self.is_element_present(By.ID, 'select-language'))

	@classmethod
	def tearDown(self):
		self.driver.quit()

	def	is_element_present(self, how, what):
		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException(): 
			self.driver.close()
			print("\nElement is missing.")
			return False
		return True