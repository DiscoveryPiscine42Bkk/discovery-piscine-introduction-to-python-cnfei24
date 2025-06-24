#!/usr/bin/env python3
num = input("Give me a number: ")
try:
    float_value = int(num)
    print("This number is integer")
except ValueError:
    print(f"This number is fload ")