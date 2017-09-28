# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()

html = html_bytes.decode("utf-8")
print(html)


def reg(html):
    reg = r'(<marquee)(.+?)(</marquee>)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist[0]


print(reg(html))
