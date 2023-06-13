from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


# Main Function
if __name__ == '__main__':

	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument('--log-level=3')

	# Provide the path of chromedriver present on your system.
	# driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.set_window_size(2560,1600)
	driver.maximize_window()

	# Send a get request to the url
	driver.get('https://www.saucedemo.com/')

	#InputUserName
	username = driver.find_element_by_id("user-name")
	username.send_keys("standard_user")
	time.sleep(3)

	#InputPassword
	password = driver.find_element_by_id("password")
	password.send_keys("secret_sauce")
	time.sleep(3)

	#ClickButtonLogin
	btnlogin = driver.find_element_by_id("login-button")
	btnlogin.click()
	time.sleep(3)
	#Expected Result Success Login
	driver.find_elements_by_xpath("//*[contains(text(), 'Swag Labs')]")
	
	print("Done")