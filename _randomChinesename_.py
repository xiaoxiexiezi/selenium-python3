#利用生成的4位随机中文保存到chinesefile.txt中

from _randomchinese_ import andstr

# def helloWorld():
#     print('hello')
#
#
#
# helloWorld()
#
#
# def fun(a, b=21, c=5):
#     print(a + b + c)
#
#
# fun(1,22)
# fun(1, 2,)
#
# print(andstr)

import datetime
now = datetime.datetime.now()


chinesefilepath = '/Users/tcw/PycharmProjects/selenium-python3/selenium-python3/chinesefile.txt'
chinesefile = open(chinesefilepath, 'a',encoding='utf8')

chinesefile.write('本次随机保存的名字为|' + andstr + '|' + str(now) + '\n')
