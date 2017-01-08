import random
import datetime
from _random_8_phone_ import random_str
now = datetime.datetime.now()

f = random.choice((130, 131, 132, 133, 134, 135, 136, 138, 139, 150, 151, 173, 180, 181, 182, 183, 185, 186, 187, 189,))
u = str(f) + str(random_str(8))
print('本次随机的手机号为：' + u + '|' + str(now) + '\n')
#生产随机手机号存入qqq.txt文件
phonefile = open("/Users/tcw/qqq.txt", 'a')

now = datetime.datetime.now()

phonefile.write('本次随机到手机号为：' + u + '|' + str(now) + '\n')

tz1 = '曲靖宣威土猪养殖项目'