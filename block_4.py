# from math import *

a = int(input())
total  = 0
M25 = 0
M10 = 0
M5 = 0
M1 = 0

while a > 0:
    while  a // 25 > 0:
        M25 += 1
        a = a - 25
    print ("M25 -", M25)
    while a // 10 > 0:
        M10 += 1
        a = a - 10
    print("M10 -", M10)
    while a // 5 > 0:
        M5 += 1
        a = a - 5
    print("M5 -", M5)
    while a // 1 > 0:
        M1 += 1
        a = a - 1
    print("M1 -", M1)

total = M25 + M10 + M5 + M1
print("Всего монет:", total)
