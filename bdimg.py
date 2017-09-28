# !/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1506569881555_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%90%B4%E5%85%B4%E9%AB%98%E7%BA%A7%E4%B8%AD%E5%AD%A6"  # 地址
host = "image.baidu.com"  # 域名
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36"

header = {'User-Agent': userAgent,
          'Referer': url,
          'Host': host}

html = requests.get(url=url, headers=header).content
print(html.decode("UTF-8"))
# save html
htmlname = "爬虫html"
savehtml = open("E:/pypic/bdimg.html", 'wb').write(html)
# 初始化html
soup = BeautifulSoup(html.decode("UTF-8"), "html.parser")
# imgs = soup.select("img.main_img.img-hover")
imgs = soup.select("img[data-imgurl]")
print(imgs)
name = 12
# for img in imgs:
#    if "http" in img['src']:
#        continue
#    else:
#        img['src'] = "http:" + img['src']

count = 1
for img in imgs:
    if count > 5:
        break
    ader = {'User-Agent': userAgent,
            'Referer': img['src'],
            'Host': img['src'].split("/")[2]
            }
    pic = requests.get(url=img['src'], headers=ader).content
    open("E:/pypic/" + str(name) + ".jpg", 'wb').write(pic)
    name += 1
