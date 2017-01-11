#coding=utf-8
import random
import datetime
from _random_8_phone_ import random_str
now = datetime.datetime.now()

f = random.choice((130, 131, 132, 133, 134, 135, 136, 138, 139, 150, 151, 173, 180, 181, 182, 183, 185, 186, 187, 189,))
u = str(f) + str(random_str(8))
print('本次随机的手机号为：' + u + '|' + str(now) + '\n')

#生成随机手机号存入qqq.txt文件 ，以utf-8形式打开文件，否则下面write写入时会提示编码错误
phonefile = open("/Users/tcw/Random number.txt", 'a',encoding='utf8')

phonefile.write('本次随机到手机号为：' + u  + '|' + str(now) + '\n')

#phonefile.write( u + '|' + str(now)  + '时间' +  '\n')
tz1 = '曲靖宣威土猪养殖项目'