class node:
    def __init__(self, before=None, cargo=None, next=None):
        self._previous = before
        self._cargo = cargo
        self._next  = next

    def __str__(self):
        return str(self._cargo) or None

class linkedList:
    def __init__(self):
        self._head = None
        self._length = 0

    def add(self, cargo):
        n = node(None, cargo, self._head)
        if self._head:
            self._head._previous = n
        self._head = n
        self._length += 1

    def search(self,cargo):
        node = self._head
        while (node and node._cargo != cargo):
            node = node._next
        return node

    def delete(self,cargo):
        node = self.search(cargo)
        if node:
            prev = node._previous
            nx = node._next
            if prev:
                prev._next = node._next
            else:
                self._head = nx
                nx._previous = None
            if nx:
                nx._previous = prev
            else:
                prev._next = None
        self._length -= 1

    def __str__(self):
        print ('Size of linked list: ',self._length)
        node = self._head
        while node:
            print (node)
            node = node._next
