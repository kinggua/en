# !/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

url = "http://search.smzdm.com/?c=home&s=rimowa"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
    'Referer': 'http://search.smzdm.com/?c=home&s=rimowa',
    'Host': 'search.smzdm.com'}

html_bytes = requests.get(url=url, headers=header)
html = html_bytes.content.decode("UTF-8")
print(html)
urls = "http://y.zdmimg.com/201609/20/57e119d1197ce1534.png"
urlb = "//y.zdmimg.com/201609/20/57e119d1197ce1534.png"

print(urlb.split("/"))
