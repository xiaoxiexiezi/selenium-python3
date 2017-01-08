import linecache
import random
z = '/Users/tcw/qqq.txt'

count = len(open(z,'rU').readlines())
print('总行数:' + str(count))

qqq = random.randint(1,count)

print('随机到第' + '|' + str(qqq) + '|' + '行')

count1 = linecache.getline(z,qqq)

count2 = count1[9:20]

print('随机到第' + '|' + str(qqq) + '|' + '的内容为'  + str(count1) )

print(count2)