import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,150))
    return generatedList

def printList(list):
    print(*list)

def mergeSort(unsortedList):

    if len(unsortedList) > 1:
        mid = int(len(unsortedList) / 2)

        lhs = unsortedList[:mid]
        rhs = unsortedList[mid:]

        return mergeLists(mergeSort(lhs), mergeSort(rhs))

    elif len(unsortedList) <= 1:
        return unsortedList

def mergeLists(listA, listB):
    listC = list()

    while len(listA) > 0 or len(listB) > 0:
        while len(listA) > 0 and len(listB) > 0:
            if listA[0] < listB[0]:
                listC.append(listA[0])
                del listA[0]
            elif listA[0] > listB[0]:
                listC.append(listB[0])
                del listB[0]
        if len(listA) != 0:
            listC.append(listA[0])
            del listA[0]
        elif len(listB) != 0:
            listC.append(listB[0])
            del listB[0]

    return listC






testlist = listGenerator(9)
print("Unsorted list: ")
printList(testlist)
print("Sorted list:")
printList(mergeSort(testlist))
