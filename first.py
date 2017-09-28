# !/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

url = "http://blog.csdn.net/eric_sunah/"
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
                     ('Referer', 'http://avatar.csdn.net/2/6/8/1_sun7545526.jpg'), ('Host', 'avatar.csdn.net')]
urllib.request.install_opener(opener)
html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)

# 初始化网页
soup = BeautifulSoup(html, "html.parser")
imgs = soup.select("div#blog_userface > a > img")

imgname = 4
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
                     ('Referer', 'http://avatar.csdn.net/2/6/8/1_sun7545526.jpg'), ('Host', 'avatar.csdn.net')]
urllib.request.install_opener(opener)
for img in imgs:
    saveimg = open("E:/pypic/" + str(imgname) + ".jpg", 'wb')
    print(img)
    newimgurl = img['src']
    print(newimgurl)
    saveimg.write(urllib.request.urlopen(newimgurl).read())
    imgname += 1
    saveimg.close()
