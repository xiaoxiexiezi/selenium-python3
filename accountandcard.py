#coding=utf-8
from selenium import webdriver
import time
from _getuser_ import count2
import re
import unittest
from selenium.webdriver.support.ui import WebDriverWait
# import selenium.webdriver.JavascriptExecutor
from selenium.webdriver.support import expected_conditions as EC

class Untitled(unittest.TestCase):
    # driver = webdriver.Chrome("/Users/tcw/chromedriver")
    driver = webdriver.Firefox()
    driver.get("https://testv2.pandai.cn/sessions/new#")
    print('网站标题信息:'+ driver.title)
    driver.implicitly_wait(20)
    time.sleep(2)
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(count2)
    time.sleep(1)
    a = count2
    print(a)
    phonefile1 = "/Users/tcw/already_registered.txt"
    count3 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
    print('总行数1:' + str(count3))


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
        print('该用户身份',assert2  )
        print('--------------')
        time.sleep(2)

    except:
        print("测试失败")
        driver.find_element_by_xpath('//a[3]/b').click()

    if assert2 == '未认证':
        driver.find_element_by_link_text(u"未认证").click()
        from _randomchinese_ import andstr
        time.sleep(2)
        driver.find_element_by_css_selector("p.afac-popup-cen2>span.two-step").click()
        time.sleep(2)
        driver.find_element_by_id("realname").send_keys(andstr) #填写姓名
        from _defins_ import getdata
        driver.find_element_by_id("idnumber").clear()
        driver.find_element_by_id("idnumber").send_keys(getdata()) #填写身份证号
        idmobile = driver.find_element_by_id('idmobile').text

        driver.find_element_by_id("captcha-button").click()

        #获取图形验证码
        js = "window.open('https://testv2.pandai.cn/home/get_captcha_text')"
        driver.execute_script(js)
        time.sleep(1)

        alltab = driver.window_handles
        print('打开了' + str(len(alltab)),'个标签')
        print('第一个标签的句柄是:',alltab[0])
        print('第二个标签的句柄是:',alltab[1])
        a = driver.switch_to_window(alltab[1])
        dr55 = driver.find_element_by_xpath("//pre").text
        print('本次图形验证码是:',dr55)
        # 获取图形验证码
        driver.switch_to.window(alltab[1])
        driver.close()
        driver.switch_to.window(alltab[0])
        # 获取图形验证码
        print('********')

        try:
            a1 = driver.find_element_by_xpath('//div[8]/h2').text
            print(a1)
            if a1 == '获取验证码成功':
                driver.find_element_by_xpath('//div[7]/button[2]').click()
                print('a1')
            elif '秒之后重新尝试' in a1:
                driver.find_element_by_xpath('//div[7]/button[2]').click()
                print('a2')
            else:
                driver.find_element_by_xpath("//fieldset/input").send_keys(dr55)
                time.sleep(3)
                driver.find_element_by_css_selector('button.confirm').click()
                time.sleep(1)
                driver.find_element_by_css_selector('button.confirm').click()

                driver.find_element_by_xpath('//div[7]/button[2]').click()
                print('else')
            print(123)
        except:
            print(444)
            driver.quit()
        time.sleep(2)


        #***********打开第二个浏览器获取短信验证码****************
        driver2 = webdriver.Chrome("/Users/tcw/chromedriver")
        driver2.get("https://testv2.pandai.cn/admin/portal/query_captcha")
        print('这是打开的第二个浏览器')
        #获取短信验证码
        time.sleep(1)
        driver2.find_element_by_id("login").clear()
        driver2.find_element_by_id("login").send_keys("develop_admin")
        driver2.find_element_by_id("password").clear()
        driver2.find_element_by_id("password").send_keys("test_123")
        driver2.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        driver2.get('https://testv2.pandai.cn/admin/portal/query_captcha')

        time.sleep(1)
        driver2.find_element_by_name("mobile").send_keys(count2)
        time.sleep(5)
        driver2.find_element_by_xpath(u"//input[@value='查询']").click()
        time.sleep(1)
        jg = driver2.find_element_by_css_selector("p.form-controls").text
        print(jg)
        jg6 = jg[-6:]
        print(jg6)
        # 获取短信验证码
        time.sleep(2)
        driver2.quit()

        time.sleep(2)
        driver.switch_to_window(alltab[0])

        driver.find_element_by_id('idcode').send_keys(jg6)
        time.sleep(1)
        driver.find_element_by_id('submission').click()


    print('*************************')

    try: #检查手机号
        assert3 = driver.find_element_by_xpath('//p[3]/a[2]').text
        print('----------------------------------')
        print('该用户手机号',assert3,'：手机号为',count2)
        print('----------------------------------')
    except:
        print()
    print('*************************')
    try:
        assert1 = driver.find_element_by_xpath("//a[contains(@href, '/verify_guides/new?step=one')]").text
        print('--------------')
        print('该用户邮箱',assert1 )
        print('--------------')
      #  driver.quit()
    except:
        print("测试失败")
    print('*************************')

    try: #检查银行卡
        assert4 = driver.find_element_by_xpath('//a[4]').text
        print('----------------------------------')
        print('该用户银行卡',assert4)
        print('----------------------------------')
        # driver.get('https://testv2.pandai.cn/users/50131/bank_accounts')
        if assert4 == '未绑定' :
            driver.find_element_by_xpath('html/body/div[3]/div[1]/div[1]/p[3]/a[4]').click()
            time.sleep(1)
            from banknum import random_banknum
            banknum = random_banknum
            driver.find_element_by_id('banknumber').clear()
            driver.find_element_by_id('banknumber').send_keys(random_banknum)
            # banknum1 = driver.find_element_by_css_selector("div.afba-img-cen1 > p").text
            print('该绑卡银行为：',banknum,'|','卡号为：',banknum)

        else:
            pass
    except:
        print('有错误了')
        driver.quit()

    # finally:
    #     driver.quit()

   # driver.quit()

if __name__ == "__main__":
    unittest.main()
