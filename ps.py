# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

url = "http://search.smzdm.com/?c=home&s=rimowa"
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'),
                     ('Referer', 'http://search.smzdm.com/?c=home&s=rimowa'), ('Host', 'search.smzdm.com')]
urllib.request.install_opener(opener)
html_bytes = urllib.request.urlopen(url).read()

html = html_bytes.decode("UTF-8")
print(html)


def reg(html):
    reg = r'({"img":")(.+?)(","title)'
    all = re.compile(reg)
    alllist = re.findall(all, html)
    return alllist
