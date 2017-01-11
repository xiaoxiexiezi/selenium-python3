import random
f = open("/Users/tcw/Random number.txt","r",encoding='utf8')
lines = f.readlines()#读取全部内容  
for line in lines:
    print(line)

f1 = '/Users/tcw/Random number.txt'
count2 = len(open(f1,'rU',encoding='utf8').readlines()) #获取文件总行数
print(count2)
# list = []
# for line in open(f1,encoding='utf8'):
#     line = line.replace('\n','').split(',')
#     lie = line.append(line[1])
# print(list)

a = random.randint(1,count2)
bcs = int(a)
print('随机到第' + str(bcs) + '行')

#
# with open(f1,'rU',encoding='utf8') as f0:
#     for a in f0:
#       tmp=a.split('：')
#
#
#     print(tmp[1])

import linecache

# for i in xran(1,a):
#     abc = random.randrange(1,a)
#     print(abc)
theline = linecache.getline(r'/Users/tcw/Random number.txt',bcs)
bbb = theline.split('：')
print('随机到第' + str(bcs) + '行{' + str(theline).strip() + '}')
print(bbb[1])

from selenium import webdriver

driver = webdriver.Chrome("/Users/tcw/chromedriver")
driver.get("https://testv2.pandai.cn/")
assert "盼贷网" in driver.title
try:
   # assert(u"未绑定", driver.find_element_by_link_text(u"未绑定").text)
    assert driver.find_element_by_css_selector("h3.title2").text,('新闻公告')
#AssertionError

    print('测试通过')
except:
    print(123)