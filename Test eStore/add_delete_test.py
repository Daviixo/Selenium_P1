import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randrange as rdm

class  Add_Delete_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/")
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()


    def test_add_remove_items(self):
        driver = self.driver
        elements_added = rdm(1,5)
        
        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        elements_removed = rdm(1,5)

        print(f'\nElements added: {elements_added}\n')
        print(f'\nElements removed: {elements_removed}\n')

        while elements_removed > elements_added:
            if elements_added > elements_removed:
                break
            else:
                elements_removed = rdm(1,5)
                print(f'\nElements removed value was higher than elements added value. New value: {elements_removed}!\n')

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
                delete_button.click()
                print('Element deleted!')
            except:
                print(f'You currently have {elements_removed} as elements removed...')
                break

        sleep(3)                    
        total_elements = elements_added - elements_removed

        if total_elements == 1:

            print(f'You have removed {elements_removed}, we now have {total_elements} element')

        elif total_elements > 1 or total_elements < 1:
            
            print(f'You have removed {elements_removed}, we now have {total_elements} elements')

        elif total_elements == 0:

            print('There are no elements :D')

        sleep(5)
        

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()


if __name__ == "__main__":
	unittest.main(verbosity = 2)