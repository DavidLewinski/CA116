#!/usr/bin/env python3

monthIn = int(input())
daysIn = int(input())

month = 30 * (monthIn - 1)
totaldays = daysIn - 1
DayOfYear = totaldays + month

DayOfWeek = DayOfYear % 7 + 1

print(DayOfWeek)
