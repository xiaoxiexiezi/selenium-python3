import requests
from bs4 import BeautifulSoup
import urllib
url = 'https://testv2.pandai.cn/admin'
data = urllib.request.urlopen(url).read()
import re
data1 = data.decode('UTF-8')
# print(data1)
aaa = re.findall('<meta name="csrf-token" content="(.+?)" />', data1)
print(aaa)
def fdfd():
    url1 = 'https://testv2.pandai.cn/admin'

    s = requests.Session()
    r1 = s.get(url1)
    print(r1.text)
    postdata = {
        'authenticity_token':aaa,
        'admin_account[login':'develop_admin',
        'admin_account[password]':'test_123',
        # 'utf8':'✓'
    }
    url2 = 'https://testv2.pandai.cn/admin/admin'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0'}
    r = s.post(url1,data=postdata,headers=headers)

    print(r.text)

    print(r.status_code)
print(fdfd())
# print(r)
# print(r.text)
from urllib import request
import json
# s = requests.Session()
# filename = 'cookie'
# login = 'https://testv2.pandai.cn/admin'
# session = requests.Session()
# f = s.get(login)
# # print(f.text)
# url = 'https://testv2.pandai.cn/admin'
# data = urllib.request.urlopen(url).read()
# import re
# data1 = data.decode('UTF-8')
# # print(data1)
# aaa = re.findall('<meta name="csrf-token" content="(.+?)" />', data1)
# print(aaa)