#coding=utf-8
from selenium import webdriver
import time
import datetime
from zdhqyzm import Simulated_Login
def run():

        # driver = webdriver.Chrome("/Users/tcw/chromedriver")
        driver = webdriver.Firefox()


        urldata = driver.get("https://testv2.pandai.cn/registers/new")
        print('网站标题信息:'+ driver.title)
        driver.implicitly_wait(20)
        # cookies1 = driver.get_cookies()
        # print(cookies1)
        # time.sleep(2)
        # cookies = requests.Session()
        #
        # # time.sleep(22222)
        # urldata1 = driver.page_source
        # token = re.findall('<meta name="csrf-token" content="(.+?)" />', urldata1)
        # print(token)
        #
        # cookies = requests.Session()
        # # geturl1 = cookies.get(url1)
        # # r2 = geturl1.cookies
        # # r3 = '; '.join(['='.join(item) for item in r2.items()])  # 格式化cookie
        # # print(r3)
        # # token = re.findall('<meta name="csrf-token" content="(.+?)" />', geturl1.text)
        # print('这是get请求后台登录后的token', token)
        #
        # postdata = {
        #         'authenticity_token': token,
        #         'admin_account[login': 'develop_admin',
        #         'admin_account[password]': 'test_123',
        #         'utf8': '✓'
        # }
        # url2 = 'https://testv2.pandai.cn/admin/sessions'
        # headers = {
        #         'Host': 'testv2.pandai.cn',
        #         'Content-Type': 'application/x-www-form-urlencoded',
        #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        #         'Accept-Encoding': 'gzip, deflate, br',
        #         'Referer': 'https://testv2.pandai.cn/admin/sessions/new',
        #         'Cookie': r3,
        #         'Upgrade-Insecure-Requests': '1',
        #         'Connection': 'keep-alive',
        #         'Cache-Control':'max-age=0',
        #         'If-None-Match':'W/"1d040ed4cc48f7d92d36b907f2815046"'
        #
        # }
        # yzmurl = 'https://testv2.pandai.cn/home/get_captcha_text'
        # geturl1 = cookies.get(yzmurl)
        # r2 = geturl1.cookies
        # r3 = '; '.join(['='.join(item) for item in r2.items()])  # 格式化cookie
        #
        #
        # postdata2 = cookies.post(yzmurl)


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

        import main
        main.set_value()

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(u1) #从_random_phone_ import u读取随机生成的手机号去注册
        driver.find_element_by_id("verification").clear()
        driver.find_element_by_id("verification").send_keys(dr55)
        driver.find_element_by_id("submit").click()
        time.sleep(1)
        jg6 = Simulated_Login()


        #获取短信验证码
        # js2="window.open('https://testv2.pandai.cn/admin/portal/query_captcha')"
        # driver.execute_script(js2)
        # time.sleep(5)
        # alltab3 = driver.window_handles
        # # print('打开了' + str(len(alltab)) +'个标签')
        # # print('第一个标签的句柄是:' + alltab3[0])
        # # print('第二个标签的句柄是:' + alltab3[1])
        # driver.switch_to.window(alltab3[1])
        # time.sleep(2)
        # driver.find_element_by_id("login").clear()
        # driver.find_element_by_id("login").send_keys("develop_admin")
        # driver.find_element_by_id("password").clear()
        # driver.find_element_by_id("password").send_keys("test_123")
        # driver.find_element_by_xpath("//button[@type='submit']").click()
        # time.sleep(1)
        # driver.get('https://testv2.pandai.cn/admin/portal/query_captcha')
        # driver.switch_to.window(alltab3[1])
        # time.sleep(1)
        # driver.find_element_by_name("mobile").send_keys(u1)
        # driver.find_element_by_xpath(u"//input[@value='查询']").click()
        # time.sleep(1)
        # jg = driver.find_element_by_css_selector("p.form-controls").text
        # # print(jg)
        # jg6 = jg[-6:]
        # print('手机验证码为：',jg6)
        # driver.close()


        # driver.switch_to_window(alltab3[0])

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
if __name__ == '__main__':

        count = int(input('输入生成次数:'))
        for i in range(count):
                run()
        print('总共注册了|' , count ,'|个用户')



