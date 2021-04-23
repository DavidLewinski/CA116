#!/usr/bin/env python3

date = int(input())

splitday = (date % 10000) // 100
splitmonth = (date // 100) // 100
splityear = (date % 100)

swapped = (splitday * 10000) + (splitmonth * 100) + (splityear)

print(swapped)
