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


def getMaxWindows(arr, k):
    if k > len(arr): return []

    results = []
    deque = Deque()

    # dequeの初期化
    for i,num in enumerate(arr[:k]):
        # 新しい値と既存の間を比較して、新しい値以下は全て削除するので、dequeの末尾は新しい値より大きい値になります。
        # dequeの先頭は最大値です。(新しい値より大きいので削除されないから。)
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        deque.enqueueBack(i)

    for i,num in enumerate(arr[k:],k):
        # dequeの先頭は最大値
        results.append(arr[deque.peekFront()])
        # ウィンドウ外にある要素は取り除きます。
        while deque.peekFront() is not None and deque.peekFront() <= i-k:
            deque.dequeueFront()
        # 現在の値とそれより小さい全てのdequeの値をチェック
        while deque.peekBack() is not None and arr[deque.peekBack()] <= num:
            deque.dequeueBack()
        
        deque.enqueueBack(i)

    # 最後のmax
    results.append(arr[deque.peekFront()])

    return results

print(getMaxWindows([34,35,64,34,10,2,14,5,353,23,35,63,23], 4))    # [64, 64, 64, 34, 14, 353, 353, 353, 353, 63]