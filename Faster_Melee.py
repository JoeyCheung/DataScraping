from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://discordapp.com/login")

elem = driver.find_element_by_name("")
elem.send_keys("")

elem.send_keys(Keys.TAB)

time.sleep(.5)

actions = ActionChains(driver)
actions.send_keys("")
actions.perform()

elem.send_keys(Keys.RETURN)

time.sleep(3.0)

driver.get("https://discordapp.com/channels/176912745461972993/232387197171400704")

time.sleep(5.0)

actions = ActionChains(driver)
actions.send_keys("@#EC @#MW @#SE")
actions.perform()

time.sleep(1.0)

actions = ActionChains(driver)
actions.send_keys(Keys.RETURN)
actions.perform()

actions = ActionChains(driver)
actions.send_keys(Keys.RETURN)
actions.perform()
