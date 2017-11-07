# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:28:36 2017

@author: kunabart
"""

def coordinateSys(): 
    while True:
        x = int(input("x = "))
        print()
        y = int(input("y = "))
        print()
        
        if x > 0 and y > 0:
            print("Pierwsza")
        elif x < 0 and y > 0:
            print("Druga") 
        elif x < 0 and y < 0: 
            print("Trzecia")
        elif x > 0 and y < 0: 
            print("Czwarta") 
        elif x == 0 and y > 0: 
            print("Nad osia odcietch")
        elif x == 0 and y < 0: 
            print("Pod osia odcietch")
        elif x < 0 and y == 0: 
            print("Na lewo od osi rzednych")
        elif x > 0 and y == 0: 
            print("Na prawood osi rzednych")
        else:
            print("Srodek układu wspolrzednych")
        
        doAnother = input("Continue? (y/n)")
        if doAnother == "n":
            break
        else:
            continue
    
coordinateSys()
            
        