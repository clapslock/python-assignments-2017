
#  Ex_3.py
#  Class_4
#
#  Created by Bartosz Kunat on 02/11/2017.
#  Copyright © 2017 Clapslock Interactive. All rights reserved.

def pascalsTraingle():

    n = int(input("Please, enter number of rows: "))
    a = []
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1, i):
            a[i].append(a[i - 1][j - 1] + a[i - 1][j])
        if (n != 0):
            a[i].append(1)
    for i in range(n):
        print("   " * (n - i), end=" ", sep=" ")
        for j in range(0, i + 1):
            #{0:6}: 0- argument index; 6- space per argument in the console
            print('{0:6}'.format(a[i][j]), end=" ", sep=" ")
        print()

#pascalsTraingle()

def recPascalsTriangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = recPascalsTriangle(n - 1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
    return result

def printrecPascalsTrangle(list):
    for i in range(len(list)):
        print("   " * (len(list) - i), end=" ", sep=" ")
        for j in range(0, i + 1):
            #{0:6}: 0- argument index; 6- space per argument in the console
            print('{0:6}'.format(list[i][j]), end=" ", sep=" ")
        print()


testList = recPascalsTriangle(5)
printrecPascalsTrangle(testList)