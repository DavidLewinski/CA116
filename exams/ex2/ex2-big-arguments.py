#!/usr/bin/env python3

import sys
s = sys.argv[1:]

i = 0
while i < len(s):
    if int(s[i]) > 50:
        print(int(s[i]))
    i = i + 1
