#!/usr/bin/env python3

n = input()
s = int(input())

words = (n + "-") * s
print(words[0: len(words) - 1])
