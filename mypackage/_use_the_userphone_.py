import random


# 随机前三位加后八位随机组合
f = random.choice((130, 131, 132, 133, 134, 135, 136, 138, 139, 150, 151, 173, 180, 181, 182, 183, 185, 186, 187, 189,))
u = str(f) + str(random_str(8))
print('本次随机的手机号为：' + u)

phonefile = open("/Users/tcw/qqq.txt", 'a')

phonefile.write('本次随机手机号为：' + u + '\n')
phonefile.close()

tz1 = '曲靖宣威土猪养殖项目'
