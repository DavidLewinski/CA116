#!/usr/bin/env python3

n = int(input())
sum = 0
a = 0

i = 0
while i < n:
    a = input()
    if a == "one":
        sum = sum + 1
    elif a == "two":
        sum = sum + 2
    elif a == "three":
        sum = sum + 3
    elif a == "four":
        sum = sum + 4
    elif a == "five":
        sum = sum + 5
    i = i + 1
print(sum)
