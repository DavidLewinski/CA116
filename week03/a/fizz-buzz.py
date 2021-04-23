#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
    numIn = i + 1
    if(numIn % 3 == 0) and (numIn % 5 == 0):
        print("fizz-buzz")
    elif numIn % 3 == 0:
        print("fizz")
    elif numIn % 5 == 0:
        print("buzz")
    else:
        print(numIn)
    i = i + 1
