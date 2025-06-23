#!/usr/bin/env python3
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
re = num1 * num2
print (num1 , "x" , num2 , "=" , re)
if re < 0:
    print("The result is negative.")
elif re > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")