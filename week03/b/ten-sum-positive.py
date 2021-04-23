#!/usr/bin/env python3

n = 10
i = 0
total = 0
while i < n:
    num = int(input())
    if num > 0:
        total = total + num
    i = i + 1
print(total)
