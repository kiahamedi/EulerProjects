#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:05:16 2020

@author: kia
"""

'''
Euler Projet 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def isMotagharen(n):
    if len(n) == 6:
        if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
            return True
    else:
        return False
    

for i in range(900,999):
    for b in range(900,999):
        if isMotagharen(str(i * b)) == True:
            la = i
            lb = b
                
            
print("For numbers: " + str(la) + " and " + str(lb))
print("You have answer: " + str(la*lb))