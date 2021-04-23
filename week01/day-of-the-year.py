#!/usr/bin/env python3

monthIn = int(input())
daysIn = int(input())

month = 30 * (monthIn - 1)
DayOfYear = daysIn + month

print(DayOfYear)
