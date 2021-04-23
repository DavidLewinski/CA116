#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if ((a + b) > c) and ((c + b) > a) and ((a + c) > b):
   print("yes")
else:
   print("no")
