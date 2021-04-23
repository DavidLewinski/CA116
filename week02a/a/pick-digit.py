#!/usr/bin/env python3

number = int(input())
digit = int(input())

number = number // (10 ** digit)
number = number % 10
print(number)
