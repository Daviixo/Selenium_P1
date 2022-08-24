import csv, unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ddt import ddt, data, unpack

def get_data(file):
    rows = []
    data_file = open(file, 'r')
    
    reader = csv.reader(data_file)
    next(reader, None)

    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    @data(*get_data("testdata.csv"))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')

        #XPATH for NO RESULTS => $x('//div[2]/div/p[@class="note-msg"]/text()').map(x => x.wholeText)

        expected_count = int(expected_count)

        if len(products) > 0:
            self.assertEqual(expected_count, len(products))
        else:
            msg = self.driver.find_element(By.XPATH,'//div[2]/div/p[@class="note-msg"]').text
            self.assertEqual('Your search returns no results.', msg)
            print(f'No results found :c Check if there is a typo for {search_value}!\n')

        print(f'Completed: We found {len(products)} products!\n')
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2)