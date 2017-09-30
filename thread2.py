# !/usr/bin/python3
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor

# 自定义线程池最大数量
pool = ThreadPoolExecutor(max_workers=11)


def your_function(imgurl, imgname):
    pass


# 将下载任务加入线程
imgs = []
for img in imgs:
    imgurl = img.url
    imgname = img.name
    pool.submit(your_function, imgurl, imgname)


