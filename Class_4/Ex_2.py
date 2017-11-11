
#  Ex_2.py
#  Class_4
#
#  Created by Bartosz Kunat on 02/11/2017.
#  Copyright © 2017 Clapslock Interactive. All rights reserved.

import time

def fibonacci(n):
    a, b = 1, 1
    
    for i in range(n-1): 
        
        a,b = b, a+b
    return a

def recFibonacci(n) :
    
    if n == 0:
        return 0 
        
    elif n == 1: 
        return 1 
    else:     
        return recFibonacci(n-1) + recFibonacci(n-2)
    
start = time.time()
fibonacciTest1 = fibonacci(12)
stop = time.time()
print(start-stop)

start = time.time()
fibonacciTest2 = recFibonacci(12)
stop = time.time()
print(start-stop)