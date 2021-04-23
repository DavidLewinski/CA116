#!/usr/bin/env python3

n = int(input())

result = ""
while n != 0:
    remainder = n % 2
    n = n // 2
    result = str(remainder) + result
print(result)
