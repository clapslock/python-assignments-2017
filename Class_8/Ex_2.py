import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,100))
    return generatedList

def printList(list):
    print (*list)

def insertionSort(unsortedList):

    for i in range(1, len(unsortedList)):
        tmp = unsortedList[i]
        k = i
        while k > 0 and tmp < unsortedList[k - 1]:
            unsortedList[k] = unsortedList[k - 1]
            k -= 1
        unsortedList[k] = tmp

    printList(unsortedList)

testList = listGenerator(10)
print("List before insertion sort: ")
printList(testList)
insertionSort(testList)
