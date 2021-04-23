#!/usr/bin/env python3

n = int(input())

t1 = 0
t2 = 1
i = 0
while i < n:
    print(t1)
    t3 = t1 + t2
    t1 = t2
    t2 = t3

    i = i + 1
