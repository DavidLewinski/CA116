#!/usr/bin/env python3

mark = int(input())

if 40 > mark:
  print("first: False")
  print("second: False")
  print("third: False")
  print("fail: True")
elif 40 <= mark <= 49:
  print("first: False")
  print("second: False")
  print("third: True")
  print("fail: False")
elif 50 <= mark <= 69:
  print("first: False")
  print("second: True")
  print("third: False")
  print("fail: False")
elif 70 <= mark:
  print("first: True")
  print("second: False")
  print("third: False")
  print("fail: False")
