#!/usr/bin/env python3
num = int(input("Enter a number less than 25 \n"))
if num > 25:
    print ("ERROR")
else:
    for i in range (num , 26):
        print("Inside the loop, my variable is" , i)