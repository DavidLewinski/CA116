#!/usr/bin/env python3

n = input()

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
null = True

i = 0
while null:
    j = 0
    while j < 26 and null:
        if n[i] == caps[j]:
            print(i)
            null = False
        j = j + 1
    i = i + 1
