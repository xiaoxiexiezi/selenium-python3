import requests
import re
url = 'https://testv2.pandai.cn/admin'

def Simulated_Login():

    '''模拟登录后台'''

    cookies = requests.Session()
    headers2 = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0'}
    url1 = 'https://testv2.pandai.cn/admin/'
    geturl1 = cookies.get(url1,headers=headers2)
    r2 = geturl1.cookies
    r3 = '; '.join(['='.join(item) for item in r2.items()]) #格式化cookie
    # print(r3)
    token = re.findall('<meta name="csrf-token" content="(.+?)" />', geturl1.text)
    print('这是get请求后台登录后的token',token)

    #拿到token后写入postdata里，下方post请求登录时需要传入第一个打开url的token
    postdata = {
        'authenticity_token':token,
        'admin_account[login':'develop_admin',
        'admin_account[password]':'test_123',
        'utf8':'✓'
    }
    url2 = 'https://testv2.pandai.cn/admin/sessions'
    headers = {
        'Host':'testv2.pandai.cn',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'gzip, deflate, br',
        'Referer':'https://testv2.pandai.cn/admin/sessions/new',
        'Cookie': r3,
        'Upgrade-Insecure-Requests':'1',
        'Connection':'keep-alive',

            }
    posturl2 = cookies.post(url2,data=postdata,headers=headers) #登录后台

    print(posturl2.text)

    status_code = posturl2.status_code
    if status_code == 200 :
        print('登录成功')
    else:
        print('登录失败')
Simulated_Login()