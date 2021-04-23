#!/usr/bin/env python3

n = int(input())
start = int(input())
numIn = start

print(numIn)
i = 1
while i < n:
    if numIn % 2 == 0:
        numIn = numIn // 2
        print(numIn)
    else:
        numIn = (3 * numIn) + 1
        print(numIn)
    i += 1
