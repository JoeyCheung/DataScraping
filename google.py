from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/webhp%3Fhl%3Den%26sa%3DX%26ved%3D0ahUKEwiuyry4w4PdAhXIqlkKHQI7C-gQPAgD")

elem = driver.find_element_by_name("identifier")
elem.send_keys("")
elem.send_keys(Keys.RETURN)

time.sleep(1.0)

elem = driver.find_element_by_name("password")
elem.send_keys("")
elem.send_keys(Keys.RETURN)

time.sleep(1.0)
driver.get("https://www.google.com/gmail/")
