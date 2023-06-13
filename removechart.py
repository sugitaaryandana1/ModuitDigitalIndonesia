from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time


# Main Function
if __name__ == '__main__':

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	# driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
	# driver = webdriver.Chrome(ChromeDriverManager().install())
	driver = webdriver.Chrome()
	driver.set_window_size(2560,1600)
	driver.maximize_window()

	# Send a get request to the url
	driver.get('https://www.saucedemo.com/')

	# Input UserName
	username = driver.find_element_by_id("user-name")
	username.send_keys("standard_user")
	time.sleep(1)

	# Input Password
	password = driver.find_element_by_id("password")
	password.send_keys("secret_sauce")
	time.sleep(1)

	# Click Button Login
	btnlogin = driver.find_element_by_id("login-button")
	btnlogin.click()
	time.sleep(1)
	# Expected Result Success Login
	driver.find_elements_by_xpath("//*[contains(text(), 'Swag Labs')]")

	# Click Button Add Chart
	btnaddchart = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
	btnaddchart.click()
	time.sleep(1)

	# Click Icon Cart
	btniconchart = driver.find_element_by_id("shopping_cart_container")
	btniconchart.click()
	time.sleep(1)

	# Click button remove
	btnremove = driver.find_element_by_id("remove-sauce-labs-backpack")
	btnremove.click()
	time.sleep(1)

	# input button Continue Shopping
	btnshopping = driver.find_element_by_id("continue-shopping")
	btnshopping.click()
	time.sleep(1)
	
	print("Done")