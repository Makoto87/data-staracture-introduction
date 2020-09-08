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

# リストを受け取り、単調減少している部分リストを返す関数を実装します。
# リストの途中で単調増加する部分が出現したら、部分リストをリセットします。
def consecutiveWalk(arr):
    stack = Stack()
    stack.push(arr[0])
    for i in arr[1:]:
        # スタックの上にある要素より、arr[i]が大きい場合、スタックをリセットします。
        if stack.peek() < i:
            # スタックがnullになるまで繰り返されます。
            while stack.peek() != None: stack.pop()
        # スタックにプッシュします。スタックは常に単調減少になっています。
        stack.push(i)

    results = []
    # 配列の先頭から追加して、順番を調整します
    while stack.peek() != None: results.insert(0,stack.pop())
    return results


print(consecutiveWalk([3,4,20,45,56,6,4,3,5,3,2])) # [5,3,2]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54])) # [64, 3, 0, -34, -54]
print(consecutiveWalk([4,5,4,2,4,3646,34,64,3,0,-34,-54,4])) # [4]