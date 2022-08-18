import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AssertionsTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")


	def test_create_new_user(self):
		#xpath for ACCOUNT $x('//div[@class="account-cart-wrapper"]/a/span/text()').map(x => x.wholeText)
		driver = self.driver
		driver.find_element(By.XPATH, '//div[@class="account-cart-wrapper"]/a/span').click()
		driver.find_element(By.LINK_TEXT, 'Log In').click()

		#xpath for CREATE AN ACCOUNT $x('//div[@class="buttons-set"]/a/span/span/text()').map(x => x.wholeText)
		create_account_button = driver.find_element(By.XPATH, '//div[@class="buttons-set"]/a/span')
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
		create_account_button.click()

		self.assertEqual('Create New Customer Account', driver.title)

		first_name = driver.find_element(By.ID, 'firstname')
		middle_name = driver.find_element(By.ID, 'middlename')
		last_name = driver.find_element(By.ID, 'lastname')
		email_address = driver.find_element(By.ID, 'email_address')
		password = driver.find_element(By.ID, 'password')
		confirm_password = driver.find_element(By.ID, 'confirmation')
		news_letter_subscription = driver.find_element(By.ID, 'is_subscribed')
	
		#xpath for REGISTER $x('//form[@class="scaffold-form"]/div/button/span/span/text()').map(x => x.wholeText)

		submit_button = driver.find_element(By.XPATH, '//form[@class="scaffold-form"]/div/button/span/span')

		self.assertTrue(first_name.is_enabled() 
		and middle_name.is_enabled()
		and last_name.is_enabled()
		and email_address.is_enabled()
		and password.is_enabled()
		and confirm_password.is_enabled()
		and news_letter_subscription.is_enabled()
		and submit_button.is_enabled())

		lets_wait = time.sleep(1)

		#we now start writing stuff
		first_name.send_keys('Test')
		lets_wait
		middle_name.send_keys('Test')
		lets_wait
		last_name.send_keys('Test')
		lets_wait
		email_address.send_keys('test3419123@test.com')
		lets_wait
		password.send_keys('Test123123')
		lets_wait
		confirm_password.send_keys('Test123123')
		lets_wait
		news_letter_subscription.click()
		lets_wait
		submit_button.click()
		time.sleep(10)


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)