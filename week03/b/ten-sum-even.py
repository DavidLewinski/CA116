#!/usr/bin/env python3

n = 10
i = 0
total = 0
while i < n:
    numIn = int(input())
    numIn = ((numIn + 1) % 2) * numIn
    total = total + numIn
    i = i + 1
print(total)
