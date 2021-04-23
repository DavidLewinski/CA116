#!/usr/bin/env python3

n = 10
i = 0

while i < n:
    num = int(input())
    if i == 0:
        pnum = num
    if num > 0:
        if num <= pnum:
            pnum = num
    i = i + 1
print(pnum)
