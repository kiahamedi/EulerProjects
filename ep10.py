#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:54:16 2020

@author: kia
"""

'''
Euler Project 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

target = 2000000

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sumDigit = 0;

for i in range(2,target):
    print("Loop in: " + str(i))
    if isPrime(i) == True:
        sumDigit += i
        
print(sumDigit)