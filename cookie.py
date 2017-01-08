#coding=utf-8
from selenium import webdriver
import re
import time
import http.cookiejar
#import http.cookies
import urllib.request
driver = webdriver.Chrome("/Users/tcw/chromedriver")
mmm = driver.get("https://testv2.pandai.cn/registers/new")
print('网站标题信息:'+ driver.title)
#driver.get("https://testv2.pandai.cn/home/get_captcha_text")
url = 'https://testv2.pandai.cn/registers/new'

cj = http.cookiejar.CookieJar()
opener1 = urllib.request.HTTPCookieProcessor(cj)
opener2 = urllib.request.build_opener(opener1)
print(opener1,opener2)

Getheaders={"Host":"testv2.pandai.cn","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36","Content-Type":"text/html; charset=utf-8"}
r = opener2.open('https://testv2.pandai.cn/')
#mcookie = r('Set-cookit')
#r = opener2.open('https://testv2.pandai.cn/home/get_captcha_text')
print(r)
#print(fd)
dr55 = driver.find_element_by_xpath("//pre").text
print('本次验证码是:' + dr55)
time.sleep(3)
driver.back()
