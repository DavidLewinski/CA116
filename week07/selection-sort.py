#!/usr/bin/env python3

a = []

s = input()
while s != "end":
    a.append(int(s))
    s = input()

i = 1
j = 0
while i < len(a):
    if a[i] < a[j]:
        j = i
    print(a[i])
    i = i + 1
