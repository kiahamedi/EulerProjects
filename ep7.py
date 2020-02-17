#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:16:47 2020

@author: kia
"""


'''
Euler Project 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

target = 10001

def checkforPrime(x):
    counter = 0
    for i in range(1,x+1):
        if x % i == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False
            

counter = 1
sumPrime = 0
while True:
    print("Now in loop: " + str(counter) + " and number of Prime: " + str(sumPrime))
    if checkforPrime(counter) == True:
        sumPrime += 1
        if sumPrime == target:
            print("Answer is: " + str(counter))
            break
    counter += 1
    