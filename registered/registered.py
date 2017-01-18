#coding=utf-8
import datetime
import time
import requests
from selenium import webdriver
import re


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
    print(randomphone())
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(u23) #从_random_phone_ import u读取随机生成的手机号去注册
    driver.find_element_by_id("verification").clear()
    driver.find_element_by_id("verification").send_keys(dr55)
    driver.find_element_by_id('invitationcode').send_keys('C5N0b')

    driver.find_element_by_id("submit").click()
    time.sleep(1)


    # '''模拟登录后台'''
    cookies = requests.Session()
    headers2 = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0'}
    url1 = 'https://testv2.pandai.cn/admin/'
    geturl1 = cookies.get(url1, headers=headers2)
    r2 = geturl1.cookies
    r3 = '; '.join(['='.join(item) for item in r2.items()])  # 格式化cookie
    # print(r3)
    token = re.findall('<meta name="csrf-token" content="(.+?)" />', geturl1.text)
    # print('这是get请求后台登录后的token',token)

    # 拿到token后写入postdata里，下方post请求登录时需要传入第一个打开url的token
    postdata = {
        'authenticity_token': token,
        'admin_account[login': 'develop_admin',
        'admin_account[password]': 'test_123',
        'utf8': '✓'
    }
    url2 = 'https://testv2.pandai.cn/admin/sessions'
    headers = {
        'Host': 'testv2.pandai.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://testv2.pandai.cn/admin/sessions/new',
        'Cookie': r3,
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',

    }
    posturl2 = cookies.post(url2, data=postdata, headers=headers)  # 登录后台
    # print(posturl2.text)
    status_code = posturl2.status_code
    if status_code == 200:
        print('模拟登录成功')
    else:
        print('模拟登录失败')
    # import linecache
    # # g = '/Users/tcw/Random number.txt'
    # z = '/Users/tcw/Random number.txt'
    # count = open(z, 'rU', encoding='utf8') # 获取文件总行数
    # # print(count.read())
    # len123 = len(count.readlines())
    # print(len123,'123123123')
    # count.close()
    # count1 = linecache.getline(z, int(len123)) #读取最后一行内容
    # print(count1)
    # phone = count1[10:21]  # 截取第10-21位手机号
    # print(phone)
    # count.close()

    # 获取短信验证码
    yzmurl = 'https://testv2.pandai.cn/admin/portal/query_captcha'
    mobile = {'mobile': u23}
    dxyzm = cookies.get(yzmurl, params=mobile)
    dxyzm7 = dxyzm.text
    dxyzm8 = dxyzm7
    p = re.compile(r'\d+')  # 正则索引为只匹配数字
    token = p.findall(dxyzm8)  # 在页面中匹配数字
    print(token)
    bcdxyzm = token[-9]  # 取倒数第9个字符串
    print(bcdxyzm)
    time.sleep(1)



    if bcdxyzm != '验证码长度不正确，请检查':

        driver.find_element_by_id("phoneverification").clear()

        driver.find_element_by_id("phoneverification").send_keys(bcdxyzm)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test123")
        driver.find_element_by_id("password2").clear()
        driver.find_element_by_id("password2").send_keys("test123")
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[2]/form/p[5]/input").click()
        time.sleep(2)
        zhzjz = driver.find_element_by_xpath("//p[4]").text
        print(zhzjz)
        time.sleep(3)
        if zhzjz == '登录盼贷旧版网站查看详情':
            now = datetime.datetime.now()
            phonefile = open("/Users/tcw/already_registered.txt", 'a',encoding='utf-8')
            phonefile.write('本次注册使用手机号为：' + u23 + '|' + str(now) + '\n' )
            phonefile.close()
            phonefile1 = "/Users/tcw/already_registered.txt"
            count2 = len(open(phonefile1,'rU',encoding='utf-8').readlines()) #获取文件总行数
            print('总行数:' + str(count2))
            phonefile.close()
        else:
            print('注册并不成功')
    else:
        print('验证码长度不正确，请检查')
        driver.quit()
    driver.quit()
if __name__ == '__main__':

        count = int(input('输入生成次数:'))
        for i in range(count):
                run()
        print('总共注册了|' , count ,'|个用户')



