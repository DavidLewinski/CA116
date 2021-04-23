#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and ((n[i]) < "0" or "9" < n[i]):
     i = i + 1

if i < len(n):
     print(n[i], i)
