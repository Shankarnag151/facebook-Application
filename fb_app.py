from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "shankarnag151@gmail.com"
pwd = "9980390042"
driver = webdriver.Chrome()
dr.maximize_window()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

elem.driver.implicitly_wait(5)
time.sleep(30)
driver.close()
