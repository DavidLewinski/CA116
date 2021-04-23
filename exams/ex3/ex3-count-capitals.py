#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()
caps = []

i = 0
while i < len(words):
    letters = words[i]
    j = 0
    while j < len(letters):
        if letters[j] >= "A" and "Z" >= letters[j]:
            caps.append(letters)
        j = j + 1
    i = i + 1

print(len(caps))
