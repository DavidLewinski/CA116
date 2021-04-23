#!/usr/bin/env python3

timetable = []
s = input()

while s != "end":
    timetable.append(s)
    s = input()

i = 0
while i < len(timetable):
    if timetable[i] == 3:
        print(" ".join(timetable[0:]))
    i = i + 1
