#coding=utf-8
from selenium import webdriver
import time
from _getuser_ import count2
import datetime
import unittest
class Untitled(unittest.TestCase):
    driver = webdriver.Chrome("/Users/tcw/chromedriver")
    driver.get("https://testv2.pandai.cn/sessions/new#")
    print('网站标题信息:'+ driver.title)
    time.sleep(2)
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(count2)
    time.sleep(2)

    phonefile1 = "/Users/tcw/already_registered.txt"
    count2 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
    print('总行数:' + str(count2))
    #phonefile1.close()


    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("test123")
    driver.find_element_by_name("commit").click()
    data1=driver.find_element_by_xpath("//div[3]/div[2]/div/div/ol/li/span").text
    data2=driver.find_element_by_xpath("//li/b").text
    print(data1 + ":" + data2)


    try:
        assert1 = driver.find_element_by_xpath("//a[contains(@href, '/verify_guides/new?step=one')]").text
        print('测试通过')
        print('该用户邮箱'+ assert1 )
      #  driver.quit()
    except:
        print("测试失败")
    try:
        assert2 = driver.find_element_by_xpath('//p[3]/a').text
        print('该用户身份' + assert2)
        driver.quit()
    except:
        print("测试失败")

    print('本次登录使用的手机号为' + str(count2))
if __name__ == "__main__":
    unittest.main()
