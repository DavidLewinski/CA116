#!/usr/bin/env python3

num = int(input())

if num == 2 or num == 3:
    print("prime")
elif num % 2 == 0 or num % 3 == 0 or num == 1:
    print("not prime")
else:
    print("prime")
