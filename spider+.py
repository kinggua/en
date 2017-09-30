# !/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import random
import requests


def gethtml(url, postdata):
    header = {'User-Agent':
                  'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
              'Referer': 'https://www.baidu.com/',
              'Host': 'sp0.baidu.com',
              'Accept': '*/*',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
              'Connection': 'keep-alive'
              }

    html_bytes = requests.get(url, headers=header, params=postdata)
    return html_bytes.content


def gettime():
    timerandom = random.randint(100, 999)
    nowtime = int(time.time())
    return str(nowtime) + str(timerandom)


def judgeinput(value, ktype):
    if ktype == "num":
        if value == "":
            return 0
        else:
            try:
                value = int(value)
                return value
            except BaseException:
                print("输入错误！")
                return False
    else:
        if value == "":
            return ""
        else:
            try:
                value = str(value)
                return value
            except BaseException:
                print("输入错误")
                return False


if __name__ == '__main__':

    keyword = ""
    pnk, pn = 0, 0

    while(True):
        keyword = input("请输入你要搜索的关键词：")
        keyword = judgeinput(keyword, "str")
        if keyword:
            break
        else:
            continue

    while(True):
        pn = input("搜索页码：")
        pnk = judgeinput(pn, "num")
        if pnk:
            pn = (pnk-1)*10
            break
        else:
            continue

    url = "https://www.baidu.com/s?"
    postdata = {
            '_': gettime(),
            'bs': keyword,
            'cb': "jQuery110207635110323506591_1495027071143",
            'csor': 18,
            'json': 1,
            'p': 3,
            'pbs': keyword,
            'pwd': keyword,
            'req': 2,
            'sid': "1432_21085_17001_20927",
            'sugmode': 2,
            'wd': keyword,
            'pn': pn # 0是第一页 10 是第二页
        }

    html = gethtml(url, postdata)
    print(html.decode("UTF-8", "ignore"))

    reshtml = open("E:/web/"+keyword+"_"+str(pnk)+".html", "wb")
    reshtml.write(html)
    reshtml.close()
