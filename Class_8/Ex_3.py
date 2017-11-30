
import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,100))
    return generatedList

def printList(list):
    print (*list)

def bubbleSort(unsortedList):

    unsortedElements = len(unsortedList)

    while unsortedElements > 0:

        for i in range(0, unsortedElements - 1):

            if unsortedList[i] > unsortedList[i + 1]:

                unsortedList[i], unsortedList[i + 1] = unsortedList[i + 1], unsortedList[i]

        unsortedElements -= 1
    printList(unsortedList)

testList = listGenerator(10)
print("Unsorted list: ")
printList(testList)
bubbleSort(testList)

