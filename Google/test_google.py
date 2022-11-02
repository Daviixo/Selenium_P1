import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def test_search(self):
        sleep(3)
        search_for = input('\n\nWhat are you looking for:\n')

        google = GooglePage(self.driver)
        google.open()
        google.search(search_for)
        google.click_submit()

        self.assertEqual(search_for, google.keyword)
        sleep(5)
        
    @classmethod
    def tearDownClass(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2)