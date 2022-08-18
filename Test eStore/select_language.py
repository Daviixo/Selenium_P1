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
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_select_language(self):
        driver = self.driver

        exposed_options = ['English', 'French', 'German']
        active_options = []

        #select_language= Select(self.driver.find_element_by_id('select-language'))

        select_language = Select(driver.find_element(By.ID, 'select-language'))
        self.assertEqual(3, len(select_language.options))

        print(f'Select: {select_language.options}')

        for option in select_language.options:
            active_options.append(option.text)
        
        self.assertListEqual(exposed_options,active_options)

        self.assertEqual('English',select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german' in self.driver.current_url)
        select_language = Select(driver.find_element(By.ID, 'select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'Report_SL', report_name = 'final_report_sl'))