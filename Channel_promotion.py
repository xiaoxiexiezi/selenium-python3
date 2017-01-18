import unittest
from selenium import webdriver
import time
import random
from mypackage._random_8_phone_ import random_str
from selenium.webdriver.support.ui  import Select
def htdl():
    driver = webdriver.Firefox()
    driver.get("https://testv2.pandai.cn/admin")
    driver.implicitly_wait(11)
    driver.find_element_by_id('login').send_keys('develop_admin')
    driver.find_element_by_id('password').send_keys('test_123')
    driver.find_element_by_xpath('//button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div/ul/li[4]/a').click()
    time.sleep(1)
    driver.find_element_by_link_text(u'管理员').click()
    time.sleep(1)
    driver.find_element_by_xpath('//h5/a').click()

    Select(driver.find_element_by_id("admin_account_roles")).select_by_visible_text(u"市场")

    f = random.choice((130, 131, 133, 134, 135, 136, 138, 139, 150, 151, 173, 180, 181, 182, 183, 185, 186, 187, 189,))
    phone = str(f) + str(random_str(8))
    print(phone)
    user = 'sc' + str(phone)
    email = 'sc' + str(phone) + '@' + str(f) + '.' + 'com' #生成邮箱
    print(email)
    driver.find_element_by_id('admin_account_login').send_keys(user)
    driver.find_element_by_id('admin_account_mobile').send_keys(phone)
    driver.find_element_by_id('admin_account_email').send_keys(email)
    driver.find_element_by_id('password').send_keys('test123')
    driver.find_element_by_id('admin_account_confirm_password').send_keys('test123')
    driver.find_element_by_name('commit').click()
    # driver.find_element_by_link_text(u'市场').click()
    # #寻找input属性以placeholder开头的a元素。其中@后面的''里的内容可以替换成元素的任意其他属性。
    # driver.find_element_by_xpath("//input[starts-with(@placeholder,'')]").send_keys('sc18354723075')












if __name__ == "__main__":
   htdl()
