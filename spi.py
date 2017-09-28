# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)


def reg(html):
    reg = r'({"img":")(.+?)(","title)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist


imgurls = reg(html)
print(imgurls)

for imgurl in imgurls:
    print(imgurl[1])

# 图片名字
imgname = 1
for imgurl in imgurls:
    saveimg = open("E:/nd/" + str(imgname) + ".jpg", 'wb')
    newimgurl = "http://www.tybai.com/" + imgurl[1].replace("\\", "")
    print(newimgurl)
    saveimg.write(urllib.request.urlopen(newimgurl).read())
    imgname += 1
    saveimg.close()
