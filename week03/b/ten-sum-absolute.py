#!/usr/bin/env python3

n = 10
total = 0
i = 0

while i < n:
    num = int(input())
    if num > 0:
        total = total + num
    else:
        num = num * -1
        total = total + num
    i = i + 1

print(total)
