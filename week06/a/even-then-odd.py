#!/usr/bin/env python3

odd = []

s = input()
while s != "end":
    num = int(s)
    if num % 2 == 0:
        print(num)
    else:
        odd.append(num)
    s = input()

i = 0
while i < len(odd):
    print(odd[i])
    i = i + 1
