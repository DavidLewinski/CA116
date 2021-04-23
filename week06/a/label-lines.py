#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(s)
    s = input()

i = 0
while i < len(a):
    print(i, len(a), (a[i]))
    i = i + 1
