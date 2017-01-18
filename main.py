#从already_registeren.txt获取已经注册过的手机号并赋值给count2
import linecache
import random
z = '/Users/tcw/Random number.txt'

count = len(open(z,'rU',encoding='utf8').readlines()) #获取文件总行数


count1 = linecache.getline(z,count)
print(count1)

count2 = count1[10:21] #截取第10-21位手机号

print(count2)
