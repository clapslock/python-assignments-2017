# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:08:38 2017

@author: kunabart
"""
import time

def fibonacci(n):
    a, b = 1, 1
    
    for i in range(n-1): 
        
        a,b = b, a+b
    return a
    
fibonacci1Test = fibonacci(10)
print(fibonacci1Test)

def recursiveFibonacci(n) :
    
    if n == 0:
        return 0 
        
    elif n == 1: 
        return 1 
    else:     
        return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
    
fibonacci2Test = recursiveFibonacci(10)
print(fibonacci2Test)