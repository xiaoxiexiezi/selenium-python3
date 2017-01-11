import random
print(random.sample(['a','b','c'],1))

import random
def randDif(k,n):
    if k>n:
        return []
    a = list(range(1,n+1))
    random.shuffle(a)
    return a[:k]
print(randDif(1,5))

import random
total = 4
li = [i for i in range(total)]
res = []
num = 1
for i in range(num):
  t = random.randint(i,total-1)
  res.append(li[t])
  li[t], li[i] = li[i], li[t]
print(res)
#其实python 已经实现这样的方法：