from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
import time


# Main Function
if __name__ == '__main__':
	driver = webdriver.Chrome(executable_path="LICENSE.chromedriver", chrome_options=options)
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	# driver = webdriver.Chrome(ChromeDriverManager().install())
	# driver = webdriver.Chrome()
	driver.set_window_size(480,360)
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

	# Click button checkout
	btncheckout = driver.find_element_by_id("checkout")
	btncheckout.click()
	time.sleep(1)

	# input form first name
	firstname = driver.find_element_by_id("first-name")
	firstname.send_keys("ini column first name")
	time.sleep(1)

	# input form last name
	lastname = driver.find_element_by_id("last-name")
	lastname.send_keys("ini column last name")
	time.sleep(1)

	# input form ziportal code
	ziporpostalcode = driver.find_element_by_id("postal-code")
	ziporpostalcode.send_keys("ini column postal code")
	time.sleep(1)

	# click button continue
	btncontinue = driver.find_element_by_id("continue")
	btncontinue.click()
	time.sleep(1)

	#Expected Invoice
	driver.find_elements_by_xpath("//*[contains(text(), 'Sauce Labs Backpack')]")

	#click Button Finish
	btncontinue = driver.find_element_by_id("finish")
	btncontinue.click()
	time.sleep(1)

	#expected result
	driver.find_elements_by_xpath("//*[contains(text(), 'Thank you for your order!')]")
	print("Done")
