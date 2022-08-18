import unittest
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class test_dynamic_element(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_compare_products_removal_alert(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1
        
        #XPATH for elements on screen = $x('//div/ul/li[1]/a/text()').map(x => x.wholeText)
        
        while len(options) < 5:
            options.clear()

            for i in range(menu):
                try:
                    options_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(options_name.text)
                    print(f'\n{options}\n')
                except:
                    print(f'\nOption number {i + 1} was NOT found :c\n')
                    tries += 1
                    driver.refresh()

        if tries == 1:
            print(f'It took {tries} try! #ThatWasQuick')
        else:
            print(f'It took {tries} tries! #NotSoQuick')
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2)