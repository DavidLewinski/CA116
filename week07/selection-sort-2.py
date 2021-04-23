#!/usr/bin/env python3

a = []                  # 25, 24, 23, 22, 21, 22, 23, 24, 25

s = input()
while s != "end":
    a.append(int(s))
    s = input()

k = int(input())

j = 0
while k < len(a):
    if a[k] < a[j]:
        j = k
    k = k + 1
print(j)
