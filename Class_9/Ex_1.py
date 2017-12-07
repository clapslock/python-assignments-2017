
import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,150))
    return generatedList

def printList(list):
    print (*list)

def quickSort(unsortedList):

    if not unsortedList:
        return []
    else:
        pivot = unsortedList[0]

        lhs = quickSort([
            x for x in unsortedList[1:] if x < pivot]
        )
        rhs = quickSort([
            x for x in unsortedList[1:] if x >= pivot
        ])
        return lhs + [pivot] + rhs

testlist = listGenerator(50)
print("Unsorted list: ")
printList(testlist)
printList(quickSort(testlist))