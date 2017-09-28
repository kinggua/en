# !/usr/bin/python3
# -*- coding: utf-8 -*-


def enroll(name, age, gender='M', hobby='tennis'):
    print("name:", name)
    print("age:", age)
    print("gender:", gender)
    print("hobby:", hobby)


enroll('jams', 12, 'hosiki')
enroll('jams', 12, hobby='hosiki')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc((1, 2, 3, 4)))


def calcd(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calcd(1, 2, 3, 4))
