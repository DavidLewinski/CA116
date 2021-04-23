#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "dog", "", "", "cat", "", "", "", "mouse"]

i = 0
total = 0
while i < len(a):
    if a[i] != "":
        total = total + 1
    i = i + 1
print(total)
