#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["", "", "mountain", "", "", "cat", "mont", "", "", "month"]
    s = "mont"

i = 0

while i < len(a):
    x = a[i]
    if s == x[:len(s)]:
        print(a[i])
        i = len(a)
    i = i + 1
