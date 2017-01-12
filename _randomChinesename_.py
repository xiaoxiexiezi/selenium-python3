#利用生成的4位随机中文保存到chinesefile.txt中

from _randomchinese_ import andstr

import datetime
now = datetime.datetime.now()


chinesefilepath = '/Users/tcw/selenium-python3/chinesefile.txt'
chinesefile = open(chinesefilepath, 'a',encoding='utf8')

chinesefile.write('本次随机保存的名字为|' + andstr + '|' + str(now) + '\n')
