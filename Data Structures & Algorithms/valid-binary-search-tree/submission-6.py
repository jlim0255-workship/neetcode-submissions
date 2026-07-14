# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use bfs traversal
        if not root:
            return True

        queue = deque([(root, float("-inf"), float("inf"))])

        while queue:
            node, low, high = queue.popleft()

            if not (low < node.val < high):
                return False
            
            if node.left:
                # the upper bound high is node.val, cannot exceed node.val
                # if node.left.val >= low:
                #     return False

                # cannot set a variable here, else we will affect the high at node.right
                # high = node.val XX
                # queue.append((node.left, low, high))
                queue.append((node.left, low, node.val))

            if node.right:
                # the lower bound low is node.val, must exceed node.val
                queue.append((node.right, node.val, high))

        return True