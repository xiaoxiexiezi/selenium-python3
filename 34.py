from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from _random_amount_ import *
driver = webdriver.Chrome('/Users/tcw/chromedriver')
driver.get("https://testv2.pandai.cn")
time.sleep(2)
oldtab = driver.current_window_handle
print(oldtab)
driver.find_element_by_link_text(u"理财").click()
driver.find_element_by_link_text(u"土猪猪猪一").click()
alltab = driver.window_handles #获得标签句柄
driver.switch_to_window(alltab[1]) #焦点第二个标签[1]
title = driver.title
print(title)
time.sleep(3)
tz2 = driver.find_element_by_css_selector("div.rec-2").text
time.sleep(3)
print(tz2)
if tz1 == tz2:
	print('页面存在,测试通过')
driver.find_element_by_xpath("//a[2]").click() #还款列表
driver.find_element_by_xpath("//a[3]").click() #投资记录
time.sleep(5)
driver.quit()