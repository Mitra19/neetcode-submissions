class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        if not self.tail:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return True
        
        i = 0
        curr = self.head
        while i < index - 1 and curr.next:
            i += 1
            curr = curr.next
            
        if curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans