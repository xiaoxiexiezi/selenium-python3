#coding=utf-8
from selenium import webdriver
import time
#from _random_phone_ import u
import datetime

driver = webdriver.Chrome("/Users/tcw/chromedriver")
driver.get("https://testv2.pandai.cn/registers/new")
print('网站标题信息:'+ driver.title)
