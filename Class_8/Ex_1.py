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

    smallestElement =
    for i in range(0, len(list) - 1):

        smallestElement = min(list[i:len(list)])
        del list[list.index(smallestElement)]
        list.insert(i, smallestElement)

    print("List sorted with 'wybieranie")
    printList(list)

testList = listGenerator(50)

selectionSort(testList)












