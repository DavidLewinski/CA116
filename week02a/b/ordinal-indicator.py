#!/usr/bin/env python3

numIn = int(input())

digit = numIn % 100

if digit == 11 or digit == 12 or digit == 13:
    print("th")
elif numIn == 1 or digit % 10 == 1:
    print("st")
elif numIn == 2 or digit % 10 == 2:
    print("nd")
elif numIn == 3 or digit % 10 == 3:
    print("rd")
else:
    print("th")
