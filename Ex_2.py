# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:16:33 2017

@author: kunabart
"""
def blNum(numberOfIterations): 
    suma = 0.0   
    for n in range (0, numberOfIterations):
        
        suma += 1.0/3.0
    print("Suma: " , suma,"\n")
    
    
blNum(3000)
blNum(30000)
blNum(300000)
blNum(3000000)