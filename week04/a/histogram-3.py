#!/usr/bin/env python3

a = input()
s = 0

i = 0
while i < len(a):
    times = a[s]
    s = s + 1
    print("*" * int(times))
    i = i + 1
