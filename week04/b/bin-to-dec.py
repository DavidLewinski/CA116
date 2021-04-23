#!/usr/bin/env python3

bin = input()
i = 0
p = 0
t = 0
while i < len(bin):
    pos = int(bin[len(bin) - i - 1])
    decimal = pos * (2 ** p)
    p = p + 1
    i = i + 1
    t = t + decimal
print(t)
