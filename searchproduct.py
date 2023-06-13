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

	# Click Search produk name Z to A
	driver.find_element_by_xpath("//select[@class='product_sort_container']/option[text()='Name (Z to A)']").click()
	time.sleep(3)

	# Expected Result
	driver.find_elements_by_xpath("//*[contains(text(), 'Test.allTheThings() T-Shirt (Red)')]")

	# Click Search produk price low to high
	driver.find_element_by_xpath("//select[@class='product_sort_container']/option[text()='Price (low to high)']").click()
	time.sleep(3)

	# Expected Result
	driver.find_elements_by_xpath("//*[contains(text(), '$7.99')]")

	# Click Search produk price high to low
	driver.find_element_by_xpath("//select[@class='product_sort_container']/option[text()='Price (high to low)']").click()
	time.sleep(3)

	# Expected Result
	driver.find_elements_by_xpath("//*[contains(text(), '$49.99')]")
	print("Done")