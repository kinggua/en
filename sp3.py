# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()

html = html_bytes.decode("utf-8")

# 初始化网页
soup = BeautifulSoup(html, "html.parser")
info = soup.find('marquee').get_text()
print(info)
