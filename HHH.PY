from Robot import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/tcw/chromedriver')

driver.get("https://testv2.pandai.cn")
# time.sleep(2)
# builder = ActionChains(driver)
# ActionChains(driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()

a123  =  driver.find_element_by_xpath("//div[2]/div/ol/li/a")
ActionChains(driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
ActionChains(driver).context_click(a123).perform()
ActionChains(driver).send_keys(Keys.DOWN)

js = driver.execute_script("arguments[0].click()",element)