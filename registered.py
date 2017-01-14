#coding=utf-8
import unittest
from selenium import webdriver
import time
import datetime
def run():

        driver = webdriver.Chrome("/Users/tcw/chromedriver")
        driver.get("https://testv2.pandai.cn/registers/new")
        print('网站标题信息:'+ driver.title)
        js="window.open('https://testv2.pandai.cn/home/get_captcha_text')"
        driver.execute_script(js)
        time.sleep(2)


        alltab = driver.window_handles
        print('打开了' + str(len(alltab)) +'个标签')
        # print('第一个标签的句柄是:' + alltab[0])
        # print('第二个标签的句柄是:' + alltab[1])
        driver.switch_to_window(alltab[1])
        dr55 = driver.find_element_by_xpath("//pre").text
        print('本次验证码是:' + dr55)

        driver.switch_to_window(alltab[1])
        driver.close()
        driver.switch_to_window(alltab[0])

        from _random_phone_ import randomphone
        u1 = randomphone()

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(u1) #从_random_phone_ import u读取随机生成的手机号去注册
        driver.find_element_by_id("verification").clear()
        driver.find_element_by_id("verification").send_keys(dr55)
        driver.find_element_by_id("submit").click()
        time.sleep(1)

        js2="window.open('https://testv2.pandai.cn/admin/portal/query_captcha')"
        driver.execute_script(js2)
        time.sleep(5)
        alltab3 = driver.window_handles
        # print('打开了' + str(len(alltab)) +'个标签')
        # print('第一个标签的句柄是:' + alltab3[0])
        # print('第二个标签的句柄是:' + alltab3[1])
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
        #print(alltab3[1])
        time.sleep(1)

        driver.find_element_by_name("mobile").send_keys(u1)
        driver.find_element_by_xpath(u"//input[@value='查询']").click()
        time.sleep(1)
        jg = driver.find_element_by_css_selector("p.form-controls").text
        print(jg)
        jg6 = jg[-6:]
        print(jg6)

        driver.close()

        driver.switch_to_window(alltab3[0])
        driver.find_element_by_id("phoneverification").clear()
        driver.find_element_by_id("phoneverification").send_keys(jg6)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test123")
        driver.find_element_by_id("password2").clear()
        driver.find_element_by_id("password2").send_keys("test123")
        driver.find_element_by_xpath("//div[2]/form/p[5]/input").click()

        now = datetime.datetime.now()
        phonefile = open("/Users/tcw/already_registered.txt", 'a',encoding='utf-8')
        phonefile.write('本次注册使用手机号为：' + u1 + '|' + str(now) + '\n' )
        phonefile.close()
        phonefile1 = "/Users/tcw/already_registered.txt"
        count2 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
        print('总行数:' + str(count2))
        phonefile.close()

        time.sleep(5)
        driver.quit()
count = int(input('输入生成次数:'))
for i in range(count):
        run()
print('总共注册了|' , count ,'|个用户')



