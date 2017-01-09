#coding=utf-8
from selenium import webdriver
import re
import time
import http.cookiejar
#import http.cookies
import urllib.request
import urllib.request, urllib.parse, urllib.error
# driver = webdriver.Chrome("/Users/tcw/chromedriver")
# mmm = driver.get("https://testv2.pandai.cn/registers/new")
# print('网站标题信息:'+ driver.title)
# #driver.get("https://testv2.pandai.cn/home/get_captcha_text")
# url = 'https://testv2.pandai.cn/registers/new'
#
# cj = http.cookiejar.CookieJar()
# opener1 = urllib.request.HTTPCookieProcessor(cj)
# opener2 = urllib.request.build_opener(opener1)
# print(opener1,opener2)
#
# Getheaders={"Host":"testv2.pandai.cn","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36","Content-Type":"text/html; charset=utf-8"}
# r = opener2.open('https://testv2.pandai.cn/')
# #mcookie = r('Set-cookit')
# #r = opener2.open('https://testv2.pandai.cn/home/get_captcha_text')
# print(r)
# #print(fd)
# dr55 = driver.find_element_by_xpath("//pre").text
# print('本次验证码是:' + dr55)
# time.sleep(3)
# driver.back()
# headers = {'User-Agent': user_agent}
user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

values = {'name': '******', 'password': '******'}
driver = webdriver.Chrome("/Users/tcw/chromedriver")
driver.get("https://testv2.pandai.cn/registers/new")
print('网站标题信息:'+ driver.title)

cookie_filename = 'cookie1.txt'
#postdata = urllib.parse.urlencode(values).encode()
headers = {'User-Agent': user_agent}
URL_ROOT = r'https://testv2.pandai.cn/registers/new'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

request = urllib.request.Request(URL_ROOT)
request1 = opener.open(request)

try:
    request1 = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)





# import urllib.request
# import urllib.parse
# import urllib.error
# import http.cookiejar
#
# cookie_filename = 'cookie.txt'
# cookie1 = http.cookiejar.LWPCookieJar(cookie_filename)
# cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
# handler2 = urllib.request.HTTPCookieProcessor(cookie1)
# opener2 = urllib.request.build_opener(handler2)
#
# get_url = 'https://testv2.pandai.cn/registers/new'  # 利用cookie请求访问另一个网址
# cookie_filename1 = 'cookie1.txt'
# #get_request = urllib.request.Request(get_url)
# cookie2 = http.cookiejar.LWPCookieJar(cookie_filename1)
# cookie1.load(cookie_filename1,ignore_discard=True,ignore_expires=True)
# handler3 = urllib.request.HTTPCookieProcessor(cookie2)
# opener3 = urllib.request.build_opener(handler3)
#
# get_url2 = 'https://testv2.pandai.cn/home/get_captcha_text'  # 利用cookie请求访问另一个网址
#
# get_request = urllib.request.Request(get_url2)
#
#
# get_response = opener.open(get_request)
#
# cookie1.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
# for item in cookie1:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)
#
# print(get_response.read().decode())
