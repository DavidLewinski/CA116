#!/usr/bin/env python3

num = int(input())

split = num % 10000
split = split // 100

print(split)
