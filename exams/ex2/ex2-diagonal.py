#!/usr/bin/env python3

import sys
s = int(sys.argv[1])
args = sys.argv[1:]

i = 0
while i < int(s):
    print((i * " ") + ".")
    i = i + 1
