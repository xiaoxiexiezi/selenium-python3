#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from _12_ import *

driver = webdriver.Chrome("/Users/tcw/chromedriver")
driver.get("https://testv2.pandai.cn/registers/new")
print('网站标题信息:'+ driver.title)
js="window.open('https://testv2.pandai.cn/home/get_captcha_text')"
driver.execute_script(js)
time.sleep(2)


alltab = driver.window_handles
print('打开了' + str(len(alltab)) +'个标签')
print('第一个标签的句柄是:' + alltab[0])
print('第二个标签的句柄是:' + alltab[1])
a=driver.switch_to_window(alltab[1])
dr55 = driver.find_element_by_xpath("//pre").text
print('本次验证码是:' + dr55)

driver.switch_to_window(alltab[1])
driver.close()
driver.switch_to_window(alltab[0])
alltab = driver.window_handles
print('打开了' + str(len(alltab)) +'个标签')
print('第一个标签的句柄是:' + alltab[0])


driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(u)

driver.find_element_by_id("verification").clear()
driver.find_element_by_id("verification").send_keys(dr55)

driver.find_element_by_id("submit").click()


js2="window.open('https://testv2.pandai.cn/admin/portal/query_captcha')"
driver.execute_script(js2)
time.sleep(5)
alltab3 = driver.window_handles
print('打开了' + str(len(alltab)) +'个标签')
print('第一个标签的句柄是:' + alltab3[0])
print('第二个标签的句柄是:' + alltab3[1])
driver.switch_to_window(alltab3[1])

time.sleep(2)
driver.find_element_by_id("login").clear()
driver.find_element_by_id("login").send_keys("develop_admin")

driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("test_123")

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(1)
driver.get('https://testv2.pandai.cn/admin/portal/query_captcha')
driver.switch_to_window(alltab3[1])
print(alltab3[1])
time.sleep(1)

driver.find_element_by_name("mobile").send_keys(u)
driver.find_element_by_xpath(u"//input[@value='查询']").click()

jg = driver.find_element_by_css_selector("p.form-controls").text
print(jg)
jg6 = jg[-6:]
print(jg6)

driver.close()

driver.switch_to_window(alltab3[0])
driver.find_element_by_id("phoneverification").send_keys(jg6)



#driver.quit()