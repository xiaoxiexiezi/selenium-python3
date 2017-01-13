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
    driver = webdriver.Chrome("/Users/tcw/chromedriver")
    driver.get("https://testv2.pandai.cn/sessions/new#")
    print('网站标题信息:'+ driver.title)
    time.sleep(2)
    driver.find_element_by_id("login").clear()
    driver.find_element_by_id("login").send_keys(count2)
    time.sleep(1)
    a = count2
    print(a)
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

    if assert2 == '未认证':
        driver.find_element_by_xpath('//a[3]/b').click()
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
        # driver.get('https://testv2.pandai.cn/home/get_captcha_text')
        time.sleep(2)

        alltab = driver.window_handles
        print('打开了' + str(len(alltab)) + '个标签')
        print('第一个标签的句柄是:' + alltab[0])
        print('第二个标签的句柄是:' + alltab[1])
        a = driver.switch_to_window(alltab[1])
        dr55 = driver.find_element_by_xpath("//pre").text
        print('本次图形验证码是:' + dr55)
        # 获取图形验证码
        driver.switch_to_window(alltab[1])
        #driver.close()
        driver.switch_to_window(alltab[0])
        alltab = driver.window_handles
        # 获取图形验证码
        print('********')
        a = driver.find_element_by_xpath('//div[8]/h2').text
        totalCount = re.sub("\D", "", a)
        print(totalCount)

        try:
            a1 = driver.find_element_by_xpath('//div[8]/h2').text
            print(a1)
            if a1 == '获取验证码成功':
                driver.find_element_by_xpath('//div[7]/button[2]').click()
            elif '秒之后重新尝试' in a:
                driver.find_element_by_xpath('//div[7]/button[2]').click()

            else:
                driver.find_element_by_css_selector("fieldset > input[type=\"text\"]").send_keys(dr55)
                time.sleep(5)
                driver.find_element_by_css_selector('button.confirm').click()
                driver.find_element_by_xpath('//div[7]/button[2]').click()
            print(123)
        except:
            print(444)
            driver.quit()

        #获取短信验证码
        js2 = "window.open('https://testv2.pandai.cn/admin/portal/query_captcha')"
        driver.execute_script(js2)
        time.sleep(2)
        alltab3 = driver.window_handles
        print('打开了' + str(len(alltab)) + '个标签')
        print('第一个标签的句柄是:' + alltab3[0])
        print('第二个标签的句柄是:' + alltab3[1])
        driver.switch_to_window(alltab3[1])
        time.sleep(1)
        driver.find_element_by_id("login").clear()
        driver.find_element_by_id("login").send_keys("develop_admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test_123")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        driver.get('https://testv2.pandai.cn/admin/portal/query_captcha')
        driver.switch_to_window(alltab3[1])
        # print(alltab3[1])
        time.sleep(1)
        driver.find_element_by_name("mobile").send_keys(count2)
        time.sleep(5)
        driver.find_element_by_xpath(u"//input[@value='查询']").click()
        time.sleep(1)
        jg = driver.find_element_by_css_selector("p.form-controls").text
        print(jg)
        jg6 = jg[-6:]
        print(jg6)
        # 获取短信验证码
        alltab5 = driver.window_handles
        driver.switch_to_window(alltab5[1])
      #  driver.close()
        driver.switch_to_window(alltab5[0])
        alltab5 = driver.window_handles

        # driver.find_element_by_id('idcode').send_keys(jg6)
        # driver.implicitly_wait(10)
        # driver.execute_script(arguments[0].click(),'javascript:void(0);')
        # driver.find_element_by_id('submission').click()

        #<!-- %input#next-step.form-control.submit{:style => "", :href => "javascript:void(0);", :type => "button", :value => "下一步", :onclick => "jumpTo('span.three-step')"}/ -->
        # try:
        #     # driver.find_element_by_id('submission').click()
        #     element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
        #                                              driver.find_element_by_xpath("//div/div/div/div[2]/p").click()))
        # finally:
        #     driver.quit()









    time.sleep(5)

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

    # finally:
    #     driver.quit()

   # driver.quit()

if __name__ == "__main__":
    unittest.main()
