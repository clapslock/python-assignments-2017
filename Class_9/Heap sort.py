
import random
import time

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,150))
    return generatedList

def printList(list):
    print (*list)

#########################################################

def selectionSort(unsortedList):

    for i in range(0, len(unsortedList) - 1):
        for j in range (i + 1, len(unsortedList)):
            if unsortedList[j] < unsortedList[i]:
                unsortedList[j], unsortedList[i] = unsortedList[i], unsortedList[j]
    return unsortedList

#########################################################

def insertionSort(unsortedList):

    for i in range(1, len(unsortedList)):
        tmp = unsortedList[i]
        k = i
        while k > 0 and tmp < unsortedList[k - 1]:
            unsortedList[k] = unsortedList[k - 1]
            k -= 1
        unsortedList[k] = tmp

    return unsortedList

#########################################################

def bubbleSort(unsortedList):

    unsortedElements = len(unsortedList)

    while unsortedElements > 0:
        for i in range(0, unsortedElements - 1):

            if unsortedList[i] > unsortedList[i + 1]:
                unsortedList[i], unsortedList[i + 1] = unsortedList[i + 1], unsortedList[i]

        unsortedElements -= 1
    return unsortedList

#########################################################

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

#########################################################

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
            if listA[0] <= listB[0]:
                listC.append(listA[0])
                del listA[0]
            elif listA[0] > listB[0]:
                listC.append(listB[0])
                del listB[0]
        if not listA:
            listC.append(listB[0])
            del listB[0]
        elif not listB:
            listC.append(listA[0])
            del listA[0]

    return listC

#########################################################

def heapsort(unsortedList):
    for i in range(int((len(unsortedList) - 2) / 2), -1, -1):
        siftdown(unsortedList, i, len(unsortedList) - 1)

    for j in range(len(unsortedList) - 1, 0, -1):
        unsortedList[j], unsortedList[0] = unsortedList[0], unsortedList[j]
        siftdown(unsortedList, 0, j - 1)
    return unsortedList


def siftdown(lst, start, end):
    topmost = start
    while True:
        child = topmost * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[topmost] < lst[child]:
            lst[topmost], lst[child] = lst[child], lst[topmost]
            topmost = child
        else:
            break

#########################################################

testList = listGenerator(450)

start = time.time()
selectionSort(testList)
print(time.time()- start)

start = time.time()
insertionSort(testList)
print(time.time()- start)

start = time.time()
bubbleSort(testList)
print(time.time()- start)

start = time.time()
quickSort(testList)
print(time.time()- start)
start = time.time()
mergeSort(testList)
print(time.time()- start)

start = time.time()
heapsort(testList)
print(time.time()- start)























