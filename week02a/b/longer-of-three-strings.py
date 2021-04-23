#!/usr/bin/env python3

A = input()
B = input()
C = input()

if (len(A) > len(B) and (len(A) > len(C))):
    print(A)
elif (len(B) > len(A) and (len(B) > len(C))):
    print(B)
else:
    print(C)
