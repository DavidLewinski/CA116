#!/usr/bin/env python3

scoreHome = int(input())
scoreAway = int(input())

if scoreHome > scoreAway:
    print("Home win")
elif scoreHome == scoreAway:
    print("Draw")
else:
    print("Away win")
