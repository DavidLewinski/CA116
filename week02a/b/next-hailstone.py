#!/usr/bin/env python3

num = int(input())

if num % 2 == 0:
    num = num // 2
    print(num)

else:
    num = (num * 3) + 1
    print(num)
