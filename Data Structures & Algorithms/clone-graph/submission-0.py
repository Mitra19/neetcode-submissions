"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mapping = {}
        queue = deque([node])
        mapping[node] = Node(node.val)
        while queue:
            curr_node = queue.popleft()
            for neighbour in curr_node.neighbors:
                if neighbour not in mapping:
                    mapping[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                mapping[curr_node].neighbors.append(mapping[neighbour])
        return mapping[node]
