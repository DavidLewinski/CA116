#!/usr/bin/env python3

n = input()

i = 0
while i < len(n) and (n[i] < "0" or "9" < n[i]):
    i = i + 1
if i < len(n):
    j = i
    while j < len(n) and (n[j] >= "0" or "9" <= n[j]):
        j = j + 1
        a = j
        while a < len(n) and (n[a] < "0" or "9" < n[a]):
            a = a + 1
        if i < len(n):
            b = a
            while b < len(n) and (n[b] >= "0" or "9" <= n[b]):
                b = b + 1
    print(n[a:b], a)
