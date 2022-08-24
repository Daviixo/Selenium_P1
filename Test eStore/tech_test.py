from msilib.schema import Condition
from time import sleep
from prettytable import PrettyTable
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MercadoLibreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://mercadolibre.com/")

    def test_get_ps5_prices(self):
        driver = self.driver
        
        country = driver.find_element(By.ID, 'GT')
        country.click()

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 5')
        search_field.submit()
        sleep(3)

        #Full XPATH for Guatemala => $x('//div[4]/ul/li/a/span[contains(text(),"Guatemala")]/text()').map(x => x.wholeText)

        location = driver.find_element(By.XPATH, '//div[4]/ul/li/a/span[contains(text(),"Guatemala")]')
        location.click()
        sleep(3)

        sort_by = driver.find_element(By.CLASS_NAME, 'andes-dropdown__display-values')
        sort_by.click()
        sleep(3)

        higher_price = driver.find_element(By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        higher_price.click()
        sleep(3)

        #Articles XPATH = $x('//div[2]/section/ol/li[1]/div/div/div[2]/div/a/h2/text()').map(x => x.wholeText)

        x = PrettyTable()
        x.field_names = ["Article", "Price"]

        for i in range(5):
            article_name = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text

            article_price_tag = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/div/span[1]/span[2]/span[1]').text
            
            article_price = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[2]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text

            article_final_price = str(article_price_tag) + str(article_price)

            #For PrettyTable

            x.add_row([article_name,article_final_price])


        print('\n\n')
        print(x)
        print('\n\n')


    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2)