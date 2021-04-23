#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()
fruits = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

i = 0
while i < len(words):
    if words[i].strip() in fruits:
        print(words[i].strip())
    i = i + 1
