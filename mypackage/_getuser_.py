#从already_registeren.txt获取已经注册过的手机号并赋值给count2
import linecache
import random
z = '/Users/tcw/already_registered.txt'

count = len(open(z,'rU',encoding='utf8').readlines()) #获取文件总行数
print('总行数:' + str(count))

qqq = random.randint(1,count) #随机1-count之间的数

print('随机到第' + '|' + str(qqq) + '|' + '行') #

count1 = linecache.getline(z,qqq) #打开文件，并获取变量qqq行 赋值给count1

count2 = count1[11:22] #截取第9-20位

print(count2)

count3 = '随机到第' + '|' + str(qqq) + '|' + '行的内容为' + '[[' + str(count1).strip() + ']]'

print(count3)