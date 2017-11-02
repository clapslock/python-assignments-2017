
#  Ex_1.py
#  Class_4
#
#  Created by Bartosz Kunat on 02/11/2017.
#  Copyright © 2017 Clapslock Interactive. All rights reserved.

import time

def factorial(n):
  m = 1
  for i in range (1, n+1):
    m *= i
  return m
  
def recFactorial(n):
    if n == 1 or n == 0 :
        end = time.time()
        return 1
    return recFactorial(n-1) * n
    
start = time.time()
factorialTest1 = factorial(20)
stop = time.time()
print(start-stop)

start = time.time()
factorialTest2 = recFactorial(20)
stop = time.time()
print(start-stop)

