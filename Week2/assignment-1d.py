#!/usr/bin/env pyhton3
#This a single line comment
#write a programme that lists all prime numbers from 1-100
#Name:Sandra Langat
#Email:langatsandra75@gmail.com
#15th feb,2023
#file name:assignment-1d.py

print("***the values below are prime numbers***")
for prime_numbers in range(1,101):
    if  prime_numbers > 1:
        for i in range(2,prime_numbers):
            if(prime_numbers % i) == 0:
                break
            else:
                print(prime_numbers)