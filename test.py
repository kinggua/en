# !/usr/bin/python3
# -*- coding: utf-8 -*-


def judgeinput(value, ktype):
    if ktype == "num":
        if value == "":
            return 0
        else:
            try:
                value = int(value)
                return value
            except BaseException:
                print("!!!!!!!!!!!!")
                return False
    else:
        if value == "":
            return ""
        else:
            try:
                value = str(value)
                return value
            except BaseException:
                print("!!!!!!!!!!!!")
                return False


if __name__ == '__main__':

    keyword = ""
    pn = 0

    while(True):
        keyword = input("请输入你要搜索的关键词：")
        keyword = judgeinput(keyword, "str")
        if keyword:
            continue
        else:
            break

    while(True):
        pn = input("搜索页码：")
        pn = judgeinput(pn, "num")
        if not pn:
            break
        else:
            continue