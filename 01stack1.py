class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.next = None

    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def pop(self):
        if self.head == None: return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def peek(self):
        if self.head is None: return None
        return self.head.data

s = Stack()

s.push(2)
print(s.peek())

s.push(4)
s.push(3)
s.push(1)
s.pop()
print(s.peek())