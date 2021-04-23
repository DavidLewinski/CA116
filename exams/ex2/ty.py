#!/usr/bin/env python3

a = [30984, 7999, 12808, 5479, 20117]
total = 0

i = 0
while i < len(a):
   total = total + (int(input()) - a[i])
   i = i + 1

print(total)
