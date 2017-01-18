#coding=utf-8
from selenium import webdriver

import time

driver = webdriver.Chrome("/Users/tcw/chromedriver")
driver.get("https://testv2.pandai.cn/registers/new")
print('网站标题信息:'+ driver.title)
driver.get("https://testv2.pandai.cn/home/get_captcha_text")
url = 'https://testv2.pandai.cn/registers/new'
dr55 = driver.find_element_by_xpath("//pre").text
print('本次验证码是:' + dr55)
time.sleep(3)
driver.back()
