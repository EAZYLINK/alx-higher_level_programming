#!/usr/bin/python3
if __name__ == "__main__":
  from calculator_1.py import add
  from calculator_1.py import sub
  from calculator_1.py import mul
  from calculator_1.py import div
  a = 10
  b = 5
  print(f"{a:d} + {b:d} = {add(a, b):d}")
  print(f"{a:d} - {b:d} = {sub(a, b):d}")
  print(f"{a:d} * {b:d} = {mul(a, b):d}")
  print(f"{a:d} / {b:d} = {div(a, b):d}")
  