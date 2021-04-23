#!/usr/bin/env python3

numIn = int(input())

lastDigit = numIn % 100

if lastDigit == 11 or lastDigit == 12 or lastDigit == 13:
    print("th")
elif numIn == 1 or lastDigit % 10 == 1:
    print("st")
elif numIn == 2 or lastDigit % 10 == 2:
    print("nd")
elif numIn == 3 or lastDigit % 10 == 3:
    print("rd")
else:
    print("th")
