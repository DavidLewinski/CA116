#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["moose", "hare", "cat", "dog", "cheetah", "elephant"]

temp = a[0]
a[0] = a[len(a) - 1]
a[len(a) - 1] = temp
