# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 # the question wants from 0 instead of -1
        
        # recursively go into the nodes
        height = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        return height
