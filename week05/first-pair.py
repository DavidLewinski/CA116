#!/usr/bin/env python3

n = input()
i = 0
j = 1
while i < len(n) - 1 and (n[i] != n[j]):
    i = i + 1
    j = j + 1
if i < len(n) - 1:
    if n[i] == n[j]:
        print(n[i] + n[j])
