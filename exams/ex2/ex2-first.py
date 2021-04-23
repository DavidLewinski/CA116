#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and (n[i] < "a" or "g" < n[i]):
    i = i + 1

if i < len(n):
    j = i
    while j < len(n) and (n[j] >= "a" and "g" >= n[j]):
        j = j + 1
    print(n[i:j])
