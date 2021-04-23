#!/usr/bin/env python3

n = input()

i = 0
j = 1
while i < len(n) - 1 and (n[1] != n[j]):
    j = j + 1
    i = i + 1
if i < len(n) - 1:
    print(n[i:j + 1])
