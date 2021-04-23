#!/usr/bin/env python3

n = int(input())
m = 386917

i = 0
while i < n:
    v = int(input())
    m = m + v * 209742 - 116952  # multiply by 209742 and subtract 116942.
    print(v * 124361)            # multiply by 124361.
    i = i + 1
print(m)
