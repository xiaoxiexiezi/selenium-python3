from random import Random
def random_str(randomlength=8):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def random_phone():
    phonefile = open("/Users/tcw/qqq.txt", 'a')

    phonefile.write('本次随机手机号为：' + u + '\n')
    phonefile.close()