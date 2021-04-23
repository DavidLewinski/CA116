#!/usr/bin/env python3

s = input()
ans = ""
num = 0

i = 0
while i < len(s):
    l = s[num]
    if l != " ":
        ans = ans + l
    num = num + 1
    ans = ans
    i = i + 1

print(ans)
