# !/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

url = "http://www.tybai.com"

html_bytes = urllib.request.urlopen(url).read()

print(html_bytes.decode("utf-8"))
