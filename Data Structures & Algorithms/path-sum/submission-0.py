# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:           # empty node -> no path
                return False
            
            # 1. Add node's value to the running sum
            current_sum += node.val
            
            # 2. Check if this is a leaf and sum matches
            if not node.left and not node.right:
                return current_sum == targetSum
            
            # 3. Otherwise, check left and right subtrees
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        return dfs(root, 0)