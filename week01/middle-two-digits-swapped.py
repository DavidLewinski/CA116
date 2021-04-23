#!/usr/bin/env python3

num = int(input())

split = num % 10000
split = split // 100

num1 = split // 10
num2 = split % 10

swapped = (num2 * 10) + num1

print(swapped)
