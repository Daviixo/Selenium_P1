import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class LastPass(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_visit_lp(self):
        print("-- Page 1 process --")
        driver = self.driver
        driver.maximize_window()
        driver.get('https://support.lastpass.com/')
        sleep(5)
        print("Website loading with no problem.")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Reports', report_name = 'final_report'))