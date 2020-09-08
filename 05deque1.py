class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None: return None
        return self.head.data

    def peekBack(self):
        if self.tail == None: return None
        return self.tail.data

    def enqueueFront(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head

        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node

    def enqueueBack(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeueFront(self):
        if self.head == None: return None

        temp = self.head
        self.head = self.head.next
        if self.head != None: self.head.prev = None
        else: self.tail = None
        return temp.data

    def dequeueBack(self):
        if self.tail == None: return None

        temp = self.tail
        self.tail = self.tail.prev

        if self.tail != None: self.tail.next = None
        else: self.head = None
        return temp.data

q = Deque()
print(q.peekFront())
print(q.peekBack())

q.enqueueBack(4)
print(q.peekFront())
print(q.peekBack())

q.enqueueBack(50)
print(q.peekFront())
print(q.peekBack())

print("dequeued :" + str(q.dequeueFront()))
print(q.peekFront())
print(q.peekBack())

q.enqueueFront(36)
q.enqueueFront(96)
print(q.peekFront())
print(q.peekBack())

print("dequeued :" + str(q.dequeueBack()))
print(q.peekFront())
print(q.peekBack())

print("Emptying")
q.dequeueBack()
q.dequeueBack()
q.dequeueBack()
q.dequeueBack()

# print("Emptying")
# q.dequeueFront()
# q.dequeueFront()
# q.dequeueFront()
# q.dequeueFront()

print(q.peekFront())
print(q.peekBack())