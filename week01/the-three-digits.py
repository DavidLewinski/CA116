#!/usr/bin/env python3

num = int(input())

x1 = num // 100
x2 = (num // 10) - (x1 * 10)
x3 = (num) - ((num // 10) * 10)

print(x1)
print(x2)
print(x3)
