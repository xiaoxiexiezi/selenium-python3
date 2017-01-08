import random
import string
print(random.randint(0,9))

print(random.choice('abcdefghijklmnopqrstuvwxyz'))

tt = random.sample('abcdefghijklmnopqrstuvwxyz',3)
print(tt)

#print(string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)).replace(' ',''))

a = random.randint(65,90)
print(a)

b = [random.choice(string.ascii_letters) for i in range(6)] #大小写随机
print(b)

c = [random.choice(string.digits) for i in range(3)]
print(c)
d = tt + c

random.shuffle(d)
print(d)
s1 = ""
s2 = s1.join(d)
print(s2)

sss = open("/Users/tcw/qqq.txt",'a')


sss.write('本次随机密码为' + s2 + '\n' )
sss.close()