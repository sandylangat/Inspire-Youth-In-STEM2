#!/usr/bin/env python3
#This is single line comment
#Assignment 10: Get the average of the numbers in a list by first entering them as input
#Name:Sandra Langat
#Email:langatsandra75@gmail.com
#16th feb,2023
#File:numbers.py

numbers = []
n = int(input("Enter the number of elements:"))
for i in range (0 , n):
    elem = int(input("Enter the elements:"))
    numbers.append(elem)
avg = sum(numbers)/n
print("The created list:",numbers)
print("The average = ",avg)

