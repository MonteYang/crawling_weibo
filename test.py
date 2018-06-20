# coding: utf-8

import requests
from lxml import etree
from pandas import DataFrame
import pandas as pd
import time


users = []
comments = []
times = []

for i in range(15):
    url = 'https://weibo.cn/comment/E3bri9IO7?uid=2609400635&rl=0&page={}'.format(str(i+2))
    headers = {
        'Cookie': '_T_WM=ee955e260f9340c4c2339730aedc0175; SUB=_2A252I8XVDeRhGeBP6VQZ9CnOwzyIHXVV7-udrDV6PUJbkdAKLVGikW1NRXHA4yla1BjRpmRllZoGonGqAgA22zHO; SUHB=0D-1Q_AbyCoJh-; SCF=AnL7HbrwFOPbhIXboHxy9LlABLUugJ5d2zxm7Vr3aD2kT9EGb4pUWNt__do1wBrHez9B7KQjoJVGraJ5Ebzq87U.; SSOLoginState=1529329029',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    r = requests.get(url, timeout=5, headers=headers)
    print('状态码:',r.status_code)
    # print(r.content)
    s = etree.HTML(r.content)
    user = s.xpath('//div[@class="c"]/a[1]/text()')[1:-1]
    users.extend(user)
    # print(users)
    comment = s.xpath('//div[@class="c"]/span[@class="ctt"]/text()[1]')
    comments.extend(comment)
    # print(comments)
    Time = s.xpath('//div[@class="c"]/span[@class="ct"]/text()')
    times.extend(Time)
    # print(time)
    time.sleep(1)
    print('正在获取第{}页'.format(str(i+2)))


print(len(users),len(comments), len(times))
data = DataFrame([users, comments, times]).T
data.to_csv('comments.csv')
pass