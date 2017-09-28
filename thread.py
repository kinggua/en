# !/usr/bin/python3
# -*- coding: utf-8 -*-
import threading
import requests
from bs4 import BeautifulSoup

# 定义url头部
url = "http://search.smzdm.com/?c=home&s=rimowa"  # 地址
host = "search.smzdm.com"  # 域名
userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"  # 模拟浏览器
header = {'User-Agent': userAgent,
          'Referer': url,
          'Host': host}


html_byte = requests.get(url=url, headers=header).content
html = html_byte.decode("UTF-8")

def aruqreurl(html):
    if None == html:
        print("error in html build")
    else:


# 定义线程
def download(imgurl, imgname):
    header = {'User-Agent': userAgent,
              'Referer': imgurl,
              'Host': imgurl.split("/")[2]}
    saveimg = open("E:/pypic" + str(imgname), "wb")
    saveimg.write(requests.get(url=imgurl, headers=header).content)
    saveimg.close()

# 创建线程池
threadpool = []
imgurls = []
imgname = 1
for imgurl in imgurls:

    th = threading.Thread(target=download, args=(imgurl, imgname))
    # 将线程加入线程池
    threadpool.append(th)
    imgname += 1

# 开始线程
for th in threadpool:
    th.start()

# 等待所有线程运行完毕
for th in threadpool:
    th.join()



