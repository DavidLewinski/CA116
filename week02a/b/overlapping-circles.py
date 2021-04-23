#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

if ((x2 - x1) ** 2) + ((y2 - y1) ** 2) < (r1 + r2) ** 2:
    print("yes")
else:
    print("no")
