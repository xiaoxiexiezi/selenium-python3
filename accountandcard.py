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
    time.sleep(1)

    phonefile1 = "/Users/tcw/already_registered.txt"
    count3 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
    print('总行数:' + str(count3))
    #phonefile1.close()


    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("test123")  #密码
    driver.find_element_by_name("commit").click()
    data1=driver.find_element_by_xpath("//div[3]/div[2]/div/div/ol/li/span").text
    data2=driver.find_element_by_xpath("//li/b").text
    print(data1 + ":" + data2)

    print('*************************')
    try:
        assert2 = driver.find_element_by_xpath('//p[3]/a').text
        print('--------------')
        print('该用户身份' + assert2  )
        print('--------------')

    except:
        print("测试失败")
        driver.find_element_by_xpath('//a[3]/b').click()

    if
    print('*************************')

    try: #检查手机号
        assert3 = driver.find_element_by_xpath('//p[3]/a[2]').text
        print('----------------------------------')
        print('该用户手机号'+assert3+'：手机号为'+str(count2))
        print('----------------------------------')
    except:
        print()
    print('*************************')
    try:
        assert1 = driver.find_element_by_xpath("//a[contains(@href, '/verify_guides/new?step=one')]").text
        print('--------------')
        print('该用户邮箱'+ assert1 )
        print('--------------')
      #  driver.quit()
    except:
        print("测试失败")
    print('*************************')

    try: #检查银行卡
        assert4 = driver.find_element_by_xpath('//a[4]').text
        print('----------------------------------')
        print('该用户银行卡' + assert4)
        print('----------------------------------')
        driver.get('https://testv2.pandai.cn/users/50131/bank_accounts')
        time.sleep(1)
        bank = driver.find_element_by_css_selector('h2').text
        banknum = driver.find_element_by_css_selector("div.afba-img-cen1 > p").text
        print('该绑卡银行为：' + bank + '|' + '卡号为：' + banknum)
        print(bank)
    except:
        print('有错误了')

    driver.quit()

if __name__ == "__main__":
    unittest.main()
