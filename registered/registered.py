#coding=utf-8
import datetime
import time

from selenium import webdriver


def run():

        # driver = webdriver.Chrome("/Users/tcw/chromedriver")
        driver = webdriver.Firefox()
        driver.get("https://testv2.pandai.cn/registers/new")
        print('网站标题信息:'+ driver.title)
        driver.implicitly_wait(20)
        js="window.open('https://testv2.pandai.cn/home/get_captcha_text')"
        driver.execute_script(js)
        time.sleep(2)
        alltab = driver.window_handles
        driver.switch_to.window(alltab[1])
        dr55 = driver.find_element_by_xpath("//pre").text
        print('本次图形验证码是:' + dr55)
        driver.switch_to.window(alltab[1])
        driver.close()
        driver.switch_to.window(alltab[0])


        from mypackage._random_phone_ import randomphone
        u23 = randomphone()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(u23) #从_random_phone_ import u读取随机生成的手机号去注册
        driver.find_element_by_id("verification").clear()
        driver.find_element_by_id("verification").send_keys(dr55)
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        from mypackage._zdhqyzm_ import  Simulated_Login
        yzm = Simulated_Login()
        if yzm != '验证码长度不正确，请检查':

            driver.find_element_by_id("phoneverification").clear()

            driver.find_element_by_id("phoneverification").send_keys(yzm)
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("test123")
            driver.find_element_by_id("password2").clear()
            driver.find_element_by_id("password2").send_keys("test123")
            time.sleep(0.5)
            driver.find_element_by_xpath("//div[2]/form/p[5]/input").click()
            now = datetime.datetime.now()
            phonefile = open("/Users/tcw/already_registered.txt", 'a',encoding='utf-8')
            phonefile.write('本次注册使用手机号为：' + u23 + '|' + str(now) + '\n' )
            phonefile.close()
            phonefile1 = "/Users/tcw/already_registered.txt"
            count2 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
            print('总行数:' + str(count2))
            phonefile.close()
        else:
            print('验证码长度不正确，请检查')
            driver.quit()
        driver.quit()
if __name__ == '__main__':

        count = int(input('输入生成次数:'))
        for i in range(count):
                run()
        print('总共注册了|' , count ,'|个用户')



