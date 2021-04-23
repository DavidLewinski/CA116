#!/usr/bin/env python3

timetable = []
s = input()

while s != "end":
    timetable.append(s)
    s = input()

i = 0
while i < len(timetable):
    tokens = timetable[i].split()
    print(tokens[3])
    i = i + 1
