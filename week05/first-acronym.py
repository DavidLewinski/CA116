#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and (n[i] < "A" or "Z" < n[i]):
    i = i + 1

if i < len(n):
    j = i
    while j < len(n) and (n[j] >= "A" and "Z" >= n[j]):
        j = j + 1
    print(n[i:j], i)
