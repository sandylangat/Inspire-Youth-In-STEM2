#!/usr/bin/env python3
#This is a single line comment
#Write a program that calculates 16% on tax icome
#Name: Sandra Langat
#Email: langatsandra75@gmail.com
#17th feb,2023
# File : bank.py
#16%  tax income on income ranging between 100k-150k
#19%  tax income tbtwn 150k - 300k
#30%  tax income on income above 300k
# 5% tax icome less than 100k

#print gross income and net income 
gross_income = int(input("enter your income :"))
if(gross_income <=100000):
    net = gross_income - (gross_income*0.05)
elif((gross_income > 100000)) & ((gross_income <= 150000)):
    net = gross_income -  (gross_income*0.16)
elif((gross_income > 150000)) & ((gross_income <= 300000)):
    net = gross_income - (gross_income*0.19)
elif(gross_income >300000):
    net = gross_income - (gross_income*0.3)

print(gross_income)
print(net)
    
