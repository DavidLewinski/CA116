#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
while i < len(a):
    if a[i] != "":
        print(a[i])
        i = len(a)
    i = i + 1
