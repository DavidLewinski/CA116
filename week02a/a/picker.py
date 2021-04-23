#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

EvenOrOdd = c % 2

print(a - (a * EvenOrOdd) + (b * EvenOrOdd))
