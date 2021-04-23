#!/usr/bin/env python3

s = input()
t = ""
i = 0

while i < len(s):
    z = s[0]
    y = s[1:(len(s) - 1)]
    x = s[len(s) - 1]
    t = x + y + z
    i = i + 1

print(t)
