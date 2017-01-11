#获取身份证号码
import re

import urllib.request
import random


def getdata():
    url = "http://www.welefen.com/lab/identify/?province=%E5%8C%97%E4%BA%AC&city=%E5%B8%82%E8%BE%96%E5%8C%BA&area=%E6%9C%9D%E9%98%B3%E5%8C%BA&year=1998&month=5&day=5&sex=%E7%94%B7"
    data = urllib.request.urlopen(url).read()
    data1 = data.decode('UTF-8')
    aaa = re.search('<p style="font-size:22px;color:red;">(?P<color>.+?)</p>',data1)
    if (aaa):
        h1user = aaa.group("color")
        print(h1user)

getdata()

def randomj():
    qi = random.randint(1,9) #随机一个数
    #print(qi)
    qu = qi * 100 #乘以100
    print(qu)
randomj()

from random import Random
def random_str(randomlength=8):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
        # print(str)
    return str;
    print(str)



random_str(8)