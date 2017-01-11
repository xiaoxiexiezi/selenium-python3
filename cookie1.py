# from selenium import webdriver
#
# driver = webdriver.Chrome("/Users/tcw/chromedriver")
#
# driver.get("http://www.87870.com/")
#
# driver.find_element_by_id("login-pop").click()
# driver.find_element_by_id("username").clear()
# driver.find_element_by_id("username").send_keys("momoka_yuwol")
# driver.find_element_by_id("password").send_keys("loveyou2007")
# #driver.find_element_by_id("vcode").send_keys("0000")
# driver.find_element_by_id("lw-submit").click()
#
# result = driver.find_element_by_xpath("//div[@id='login-widow']/div[2]/div/div/div").text
# result = driver.find_element_by_xpath("//div[@id='login-widow']/div[2]/div/div/div").text
#
# print (result)

import re

import urllib.request


def getdata():
    url = "http://www.welefen.com/lab/identify/?province=%E5%8C%97%E4%BA%AC&city=%E5%B8%82%E8%BE%96%E5%8C%BA&area=%E6%9C%9D%E9%98%B3%E5%8C%BA&year=1998&month=5&day=5&sex=%E7%94%B7"
    data = urllib.request.urlopen(url).read()
    data1 = data.decode('UTF-8')
    aaa = re.search('<p style="font-size:22px;color:red;">(?P<color>.+?)</p>',data1)
    if (aaa):
        h1user = aaa.group("color")
        print(h1user)

getdata()
