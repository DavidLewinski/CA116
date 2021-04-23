#!/usr/bin/env python3

i = 0
s = input()
ans = ""
num = len(s) - 1

while i < len(s):
    l = s[num]
    ans = ans + l
    num = num - 1
    i = i + 1

print(ans)
