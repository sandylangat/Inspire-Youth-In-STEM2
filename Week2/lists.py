#!/usr/bin/env python3
#This is a single line comment
#Program to write lists
#Name:Sandra Langat
#Email:langatsandra75@gmail.com
#File:list.py
#list of name
names=("James","John","Peter","Gloria","Alex")

#accessing items in a list
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])

#lists of fruits
fruits=["Mango","oranges","Pinapples","passion","banana"]
print(fruits)
print(fruits[3])
print("my favourite fruit is:",fruits[1])
print(fruits[1].upper())

#adding two lists
vegetables=["kales","spinach","pigweed","carrots","onions","broccoli"]
stationery=["pens","rubber","sharpener","ruler","scissors","stapler","glue"]
shoppings=vegetables+stationery
print(shoppings)
print(shoppings[5])

#for-looping until ikt stopped - listing items individually
for vegetable in vegetables:
    print(vegetable)

for shopping in shoppings:
    print(shopping)

#using a list to make a sentence
print("my name is" + names[3] + "and my favourte fruit is" + fruit [1])