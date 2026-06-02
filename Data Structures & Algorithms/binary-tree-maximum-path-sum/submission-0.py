# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def pathsum(root):
            if not root:
                return 0
            left = max(0, pathsum(root.left))
            right = max(0, pathsum(root.right))
            self.max_sum = max(self.max_sum, left + right + root.val)
            return max(left, right) + root.val
        pathsum(root)
        return self.max_sum