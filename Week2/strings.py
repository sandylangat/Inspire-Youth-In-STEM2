#!/usr/bin/env python3
#This is a single line comment
#Strings operations in python
#Name:Sandra Langat
#Email:langatsandra75@gmail.com
#File name:strings.py

poem = """This a poem about nothing it is funy how people laugh about nothing"""

print(poem)
print(len(poem))

name1 = "Sandra"
name2 = "Langat"
full_name =name1 +" "+name2
age = 20

print("My name is" ,full_name ,"and my age is" ,str(age),("years old"))

#Format the string
print("my name is {} and I am {} year old".format(full_name,age)) #best method

#Escape characters
#\t --->tab(spacing)
#\n -->a new line 
print("Hello from Sandy\n How are you\n I am fine")
print("Hello from Sandra \t How are you \t I am Fine")