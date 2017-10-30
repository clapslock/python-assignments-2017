# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:08:38 2017

@author: kunabart
"""
import time

def silnia1():
  start = time.time()
  n = int(input("Podaj liczb z której chesz obliczy silnie: \n"))
  m = 1
  for i in range (1, n+1):
    m *= i
  print("Silnia z", n , "to", m) 
  end = time.time()
  print (end - start)
  
def silnia(n): 
    start = time.time()
    if n == 1 or n == 0 :
        end = time.time()
        return 1
    end = time.time()
    print (end - start)
    return silnia(n-1) *n
    
    
silniaTest =  silnia(5)
print(silniaTest)

silnia1()
