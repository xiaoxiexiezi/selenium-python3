banknum = ([
    # 广发
    '622568372600001',

    # 工商
    '622202100111624',
    '622202380301329',

    # 兴业
    '62290933328011',

    # 深发展银行(平安银行)
    '622538006959',

    # 中国银行
    '60138201000150',

    # 中国农业银行
    '622848001827373',

    # ZCZP0800-无密快捷协议;ZTBB0G00-无密投资;ZHKB0H01-无密还款
    # mer_bind_agreement

    # 兴业
    '62290936371195',

    # 邮政
    '621098100001835',

    # 建行
    '622700381417017'

    # 平安银行
    '623058000002438'
    ])

from random import choice
from _random_8_phone_ import random_str
print(choice(banknum) + random_str(4))

print(random_str(4))