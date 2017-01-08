#手机号后八位随机
import random
a = random.randint(00000000,99999999)
print(a)

#充值金额随机
qi = random.randint(1,99) #随机一个数
#print(qi)
qu = qi * 100 #乘以100
print(qu)

#随机前三位加后八位随机组合
f = random.choice((130,131,132,133,134,135,136,138,139,150,151,173,180,181,182,183,185,186,187,189,))
u = str(f) + str(a)
print(u)

tz1 = '曲靖宣威土猪养殖项目'
print(tz1)