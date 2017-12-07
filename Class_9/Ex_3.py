import random

def listGenerator(n):
    generatedList = list()

    for n in range(0, n):
        generatedList.append(random.randint(0,150))
    return generatedList

def printList(list):
    print(*list)

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


testList = listGenerator(50)
print("List before sorting:")
printList(testList)
print("Sorted list: ")
printList(heapsort(testList))