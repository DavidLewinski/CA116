#!/usr/bin/env python3

import sys
years = sys.stdin.read().split()
a = []
x = False

i = 0
while i < len(years) and not x:
    if int(years[i]) >= 100:
        print(years[i].strip())
        x = True
    i = i + 1

if x is False:
    print("none")
