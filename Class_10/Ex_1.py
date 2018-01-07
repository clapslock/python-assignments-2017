
class MyNode:

    def __init__(self, score, name):
        self.score = score
        self.name = name
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addAtBeginning(self, score, name):

        n = MyNode(score, name)
        self.count += 1

        if self.head != None:
            n.next = self.head
            self.head = n
        else:
            self.head = n
        if self.tail == None:
            self.tail = n

    def addAtEnd(self, score, name):

        n = MyNode(score, name)
        self.count += 1

        if self.tail != None:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

        if self.head == None:
            self.head = n

    def addAtIndex(self, index, score, name):

        n = MyNode(score, name)
        tempNode = self.head
        self.count += 1

        if index == 0:
            self.addAtBeginning(score, name)
        elif index >= self.count:
            self.addAtEnd(score, name)
        elif index > 0 and index < self.count:
            for i in range(1, index):
                tempNode = tempNode.next

            tempNode2 = tempNode.next
            n.next = tempNode.next
            tempNode.next = n
            n.prev = tempNode
            tempNode2.prev = n

    def deleteLast(self):
        if self.tail != None:
            n = self.tail
            self.tail = n.prev
            n.prev = None
            n.next = None
            self.count -= 1

    def deleteFirst(self):
        if self.head != None:
            n = self.head
            self.head = n.next
            n.next = None

    def printFromStart(self):
        n = self.head

        for i in range(self.count):
            print(n.name)
            if n.next != None:
                n = n.next
            else:
                break

    def printFromEnd(self):
        n = self.tail

        for i in range(self.count):
            print(n.name)

            if n.prev != None:
                n = n.prev
            else:
                break

    def findHighestScore(self):
        hs = 0
        n = self.head

        for i in range(self.count):
            if int(n.score) > hs:
                hs = n.score

            if n.next != None:
                n = n.next
            else:
                break
        return hs

ll = MyLinkedList()
ll.addAtBeginning(1, "Bartek")
ll.addAtEnd(2, "Chloe")
ll.addAtEnd(21, "Lana")
ll.addAtBeginning(101, "Ellie")
ll.addAtIndex(2, 42, "Mikky B")
ll.printFromStart()
print()
ll.printFromEnd()
print(ll.findHighestScore())









