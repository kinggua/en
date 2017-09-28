# !/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://blog.csdn.net/eric_sunah/"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Referer': 'http://blog.csdn.net/eric_sunah/',
    'Host': 'blog.csdn.net'}
html_bytes = requests.get(url=url, headers=header)
html = html_bytes.content.decode("UTF-8")
print(html)

# 初始化网页
soup = BeautifulSoup(html, "html.parser")
imgs = soup.select("div#blog_userface > a > img")

imgname = 3

for img in imgs:
    saveimg = open("E:/pypic/" + str(imgname) + ".jpg", 'wb')
    print(img)
    newimgurl = img['src']
    print(newimgurl)
    newheader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
        'Referer': newimgurl,
        'Host': 'avatar.csdn.net'}
    saveimg.write(requests.get(url=newimgurl, headers=newheader).content)
    imgname += 1
    saveimg.close()
