#!/usr/bin/env python3
#This is a single line comment
#Python program to
#Name: Sandra Langat
#Email:langatsandra75@gmail.com
#17th Feb,2023
# File: conditions.py

#If........else
age = 17
gender = "male"

if (age < 18):
    print("You are still young")
else:
    print("You should get an ID")

#compound/multiple conditions
if ((age > 30 & gender == "male")):
    print("You qualify for a loan")
else:
    print("No loan for you")

fav_colour = "green"
age = 22
if((fav_colour == "green") | (age <= 20)):
    print("Happy Birthday")
else:
    print("No happy birthday present for you")

