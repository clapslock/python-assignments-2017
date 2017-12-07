import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,100))
    return generatedList

def printList(list):
    print (*list)

def selectionSort(list):
    print("Generated list before sorting:")
    printList(list)

    for i in range(0, len(list) - 1):
        for j in range (i + 1, len(list)):
            if list[j] < list[i]:
                list[j], list[i] = list[i], list[j]

    print("List sorted with 'selection sort")
    printList(list)

testList = listGenerator(50)

selectionSort(testList)












