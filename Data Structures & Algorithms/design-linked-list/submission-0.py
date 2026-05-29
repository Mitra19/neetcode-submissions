class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyLinkedList:
    def __init__(self):
        self.min = Node(-1)
        self.max = Node(-1)
        self.min.right = self.max
        self.max.left = self.min

    def get(self, index: int) -> int:
        count = 0
        curr = self.min.right
        while curr != self.max:
            if count == index:
                return curr.val
            else:
                count += 1
                curr = curr.right
        return -1 
    def get_node(self, index: int) -> Node:
        count = 0
        curr = self.min.right
        while curr != self.max:
            if count == index:
                return curr
            else:
                count += 1
                curr = curr.right
        return Node(-1)
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        prv, nxt = self.min, self.min.right
        prv.right = node
        nxt.left = node
        node.right = nxt
        node.left = prv

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prv, nxt = self.max.left, self.max
        prv.right = node
        nxt.left = node
        node.right = nxt
        node.left = prv

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.get_node(index-1)
        new_node = Node(val)
        if node.val != -1:
            prv, nxt = node, node.right
            prv.right = new_node
            nxt.left = new_node
            new_node.right = nxt
            new_node.left = prv


    def deleteAtIndex(self, index: int) -> None:
        node = self.get_node(index)
        if node.val != -1:
            prv, nxt = node.left, node.right
            prv.right = nxt
            nxt.left = prv
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)