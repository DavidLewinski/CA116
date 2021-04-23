#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["moose", "hare", "cat", "dog", "cheetah", "elephant"]
    i = 1
    j = 2

temp = a[i]
a[i] = a[j]
a[j] = temp
