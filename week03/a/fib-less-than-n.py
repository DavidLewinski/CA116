#!/usr/bin/env python3

maxNum = int(input())

t1 = 0
t2 = 1

while t1 < maxNum:
    print(t1)
    t3 = t1 + t2
    t1 = t2
    t2 = t3
