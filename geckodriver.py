from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
from _random_amount_ import qu
from _getuser_ import count2
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("https://testv2.pandai.cn")
time.sleep(2)
# builder = ActionChains(driver)
# ActionChains(driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.CONTROL).perform()
# driver.find_element_by_xpath("//div[6]/div[2]/div/p[2]").send_keys(Keys.COMMAND,'t')
# #id = cp 元素的文本信息
data=driver.find_element_by_xpath("//div[6]/div[2]/div/p[2]").text
print('网站标题信息:'+ driver.title)
print('网站底部信息:'+ data) #打印信息
time.sleep(2)
 # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# source = open("/Users/tcw/qqq.txt",'r')#打开用户名文件
# ur = source.readline()#讲user.txt赋值给ur
#source.close()#关闭文件
driver.find_element_by_link_text(u"首页").click()
driver.find_element_by_link_text(u"登录").click()
time.sleep(2)
driver.find_element_by_id("login").send_keys(count2)
time.sleep(2)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("test123")
driver.find_element_by_name("commit").click()
# data1=driver.find_element_by_xpath("//div[3]/div[2]/div/div/ol/li/span").text
# data2=driver.find_element_by_xpath("//li/b").text
# print(data1 + ":" + data2)
# driver.find_element_by_xpath(u"//a[contains(text(),'充值')]").click()
# driver.find_element_by_id("charge-amount1").clear()
# driver.find_element_by_id("charge-amount1").send_keys(qu)
# print('本次充值' + str(qu) + '元')
# driver.find_element_by_xpath("//input[@id='']").click()
# driver.find_element_by_id("btn").click()
# driver.find_element_by_id("verifyCode").clear()
# driver.find_element_by_id("verifyCode").send_keys("1234")
# driver.find_element_by_id("btn2").click()
# time.sleep(8)
# driver.find_element_by_xpath("//li[5]/a").click()
# data3=driver.find_element_by_xpath("//div[3]/div[2]/div/div/ol/li/span").text
# data4=driver.find_element_by_xpath("//li/b").text
# print('本次充值' + str(qu) + '元,现账户余额为' + ":" + data4)
# at = re.sub('[^\d\+]','',data4)
# at1=50000
# try:
#     print('result:{}元'.format(at))
# except:
#     print('result:error')
#s=int(data4)-int(data2)
#print(s)

driver.find_element_by_link_text(u"理财").click()
driver.find_element_by_link_text(u"土猪猪猪一").click()

alltab = driver.window_handles
print('打开了' + str(len(alltab)) +'个标签')
print('第一个标签的句柄是:' + alltab[0])
print('第二个标签的句柄是:' + alltab[1])



driver.switch_to_window(alltab[0])
driver.close()
driver.switch_to_window(alltab[1])
alltab = driver.window_handles
print('打开了' + str(len(alltab)) +'个标签')
print('第一个标签的句柄是:' + alltab[0])

tz2 = driver.find_element_by_css_selector("div.rec-2").text
time.sleep(3)
if tz1 == tz2:
    print('页面存在,测试通过')

driver.find_element_by_link_text(u"还款列表").click() # 还款列表
driver.find_element_by_link_text(u"投资记录").click() # 投资记录

driver.quit()