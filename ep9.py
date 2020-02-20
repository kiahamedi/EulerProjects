#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:39:31 2020

@author: kia
"""


'''
Euler Project 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

target = 1000

def checkPythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
def checkForAns(a,b,c):
    if a + b + c == target:
        return True
    else:
        return False

for a in range(1, int(target / 2)):
    for b in range(a , int(target / 2)):
        for c in range(b , int(target / 2)):
            if checkPythagorean(a,b,c) == True:
                if checkForAns(a,b,c) == True:
                    print("Answer is a:" + str(a) +" b:"+ str(b) +" c:"+ str(c))
                    print("Answer is: " + str(a*b*c))
                    exit()
            else:
                print("a:" + str(a) +" b:"+ str(b) +" c:"+ str(c))
                continue
            
            