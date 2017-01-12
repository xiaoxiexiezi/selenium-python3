import unittest
from selenium import webdriver
import time
class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/tcw/chromedriver")
        #self.driver.implicitly_wait(30)
        self.get = "https://testv2.pandai.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled1(self):
        driver = self.driver
        driver.get("https://testv2.pandai.cn/users/52919")
        driver.find_element_by_id("login").send_keys('18611173914')
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test123")
        driver.find_element_by_name("commit").click()
        time.sleep(2)

        bs2 = driver.find_element_by_css_selector("span.spanView.off_right").text

        bs1 = driver.find_element_by_xpath("//div/div/span").text


        #关闭免密投标
        def mmtzoff():
            if bs1 == '开':
                driver.find_element_by_css_selector("span.cicle_btn").click()
                driver.find_element_by_id("passWord").send_keys("123456")
                driver.find_element_by_id("btn").click()
                driver.find_element_by_id("verifyCode").send_keys("1234")
                driver.find_element_by_id("btn2").click()
                time.sleep(3)
                ok = driver.find_element_by_css_selector("p.pull-left.pay-success1-word > span").text
                if ok == '解绑协议成功!':
                    print('本次操作后免密投标功能已经被关闭了')

            else:
                print('当前免密投标功能已经~~~关闭~~~')
        mmtzoff()


        #开启免密投标
        def mmtzopen():
            if bs2 == '关':
                driver.find_element_by_css_selector("span.cicle_btn").click()
                driver.find_element_by_id("passWord").send_keys("123456")
                driver.find_element_by_id("btn").click()
                driver.find_element_by_id("verifyCode").send_keys("1234")
                driver.find_element_by_id("btn2").click()
                time.sleep(3)
                ok = driver.find_element_by_css_selector("p.pull-left.pay-success1-word > span").text
                if ok == '协议签订成功!':
                     print('本次操作后，免密投标功能已被打开了')

            else:
                print('当前免密投标功能已经~~~开启~~~')
        mmtzopen()




if __name__ == "__main__":
    unittest.main()
