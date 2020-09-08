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

def reverse(arr):
    stack = Stack()
    for i in arr:
        stack.push(i)
    
    reversed = []
    while stack.peek() != None:
        reversed.append(stack.pop())
    return reversed


arr = [1,2,3,4,5,6]
print(reverse(arr))