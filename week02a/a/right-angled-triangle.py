#!/usr/bin/env python3

hyp = int(input())
length1 = int(input())
length2 = int(input())

CheckHyp = hyp ** 2
CheckLength = (length1 ** 2) + (length2 ** 2)

triangle = CheckHyp == CheckLength

print(triangle)
