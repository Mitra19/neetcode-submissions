class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # {key: node}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node:Node):
        nxt, prv = self.right, self.right.prev
        nxt.prev = node
        prv.next = node
        node.next = nxt
        node.prev = prv

    def remove(self, node: Node):
        nxt, prv = node.next, node.prev
        nxt.prev = prv
        prv.next = nxt
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        if key not in self.cache:
            self.cache[key] = node
        else:
            self.remove(self.cache[key])
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)