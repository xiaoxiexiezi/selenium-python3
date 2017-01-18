#coding=utf-8
import time
import unittest

from selenium import webdriver


class Untitled(unittest.TestCase):

        driver = webdriver.Chrome("/Users/tcw/chromedriver")
        driver.get("https://testv2.pandai.cn/registers/new")
        print('网站标题信息:'+ driver.title)
        js="window.open('https://testv2.pandai.cn/home/get_captcha_text')"
        driver.execute_script(js)
        time.sleep(2)
        js.windows.focus()

        time.sleep(5)