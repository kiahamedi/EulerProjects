#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:50:29 2020

@author: kia
"""

'''
Euler Projet 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


target = 600851475143

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(2,target+1):
    if isPrime(i) and target % i == 0:
        print(i)