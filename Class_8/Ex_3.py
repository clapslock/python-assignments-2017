import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,150))
    return generatedList

def printList(list):
    print (*list)

def bubbleSort(unsortedList):

    print("Generated list before sorting: ")
    printList(unsortedList)

    unsortedElements = len(unsortedList)

    while unsortedElements > 0:
        for i in range(0, unsortedElements - 1):

            if unsortedList[i] > unsortedList[i + 1]:
                unsortedList[i], unsortedList[i + 1] = unsortedList[i + 1], unsortedList[i]

        unsortedElements -= 1
    print("List sorted with bubble sort: ")
    printList(unsortedList)

bubbleSort(listGenerator(50))
