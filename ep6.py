#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:35:30 2020

@author: kia
"""

'''
Euler Project 6

The sum of the squares of the first ten natural numbers is,
12+22+...+102=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)2=552=3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

target = 100


sum = 0
for i in range(target+1):
    sum += i**2


s = 0
for i in range(target+1):
    s += i

ans = s**2 - sum
print("Answer is: " + str(ans))

    
