#!/usr/bin/env python3

s = input()
num = len(s) - 1

total = 0
i = 0

while i < len(s):
    total = total + int(s[num])
    num = num - 1
    i = i + 1
print(total)
