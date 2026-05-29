class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = Node(-1)
        self.next = Node(-1)
        self.curr = Node(homepage)
        self.prev.right = self.curr
        self.next.left = self.curr
        self.curr.left = self.prev
        self.curr.right = self.next
        

    def visit(self, url: str) -> None:
        prv, nxt = self.curr, self.next
        node = Node(url)
        prv.right = node
        node.right = nxt
        node.left = prv
        nxt.left = node
        self.curr = node
        

    def back(self, steps: int) -> str:
        count = 0
        while self.curr != self.prev:
            if count == steps:
                return self.curr.val
            else:
                self.curr = self.curr.left
                count+=1
        self.curr = self.prev.right
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        count = 0
        while self.curr != self.next:
            if count == steps:
                return self.curr.val
            else:
                self.curr = self.curr.right
                count+=1
        self.curr = self.next.left
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)