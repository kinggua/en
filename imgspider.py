# !/usr/bin/python3
# -*- coding: utf-8 -*-

# with requests
import requests
from bs4 import BeautifulSoup

url = "http://search.smzdm.com/?c=home&s=rimowa"  # 地址
host = "search.smzdm.com"  # 域名
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"  # 模拟浏览器
header = {'User-Agent': userAgent,
          'Referer': url,
          'Host': host}

html = requests.get(url=url, headers=header).content
print(html.decode("UTF-8"))
# save html
htmlname = "爬虫html"
# savehtml = open("E:/pypic/" + str(htmlname) + ".html", 'wb').write(html)

# 初始化html
soup = BeautifulSoup(html.decode("UTF-8"), "html.parser")
imgs = soup.select("body img")
name = 12
for img in imgs:
    if "http" in img['src']:
        continue
    else:
        img['src'] = "http:" + img['src']

print(imgs)
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
