#!/usr/bin/env python3

n = 10
total = 0
i = 0
while i < n:
    num = int(input())
    if num < 0:
        digit = (num * -1) % 10
        total = total + digit
    else:
        digit = num % 10
        total = total + digit
    i = i + 1
print(total)
