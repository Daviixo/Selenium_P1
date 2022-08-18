import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    @classmethod 
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://jira.ops.expertcity.com/browse/")

    def test_select_language(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'Test')
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Report_SL', report_name = 'final_report_sl'))