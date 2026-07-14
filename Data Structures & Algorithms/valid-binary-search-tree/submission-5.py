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

            # naive wrong, the whole left and right subtree must be bst as well
            # if node.left or node.right:
            #     if node.left.val >= node.val or node.right.val <= node.val:
            #         return False

            # false condition
            # low = min(low, node.val)
            # high = max(high, node.val)
            # if node.val > high or node.val < low:
            #     return False

            if not (low < node.val < high):
                return False
            
            if node.left:
                # the upper bound high is node.val, cannot exceed node.val
                # if node.left.val >= low:
                #     return False

                # high = node.val
                # queue.append((node.left, low, high))
                queue.append((node.left, low, node.val))

            if node.right:
                # the lower bound low is node.val, must exceed node.val
                # low = node.val

                # if node.right.val <= high:
                #     return False
                
                # queue.append((node.right, low, high))
                queue.append((node.right, node.val, high))

        return True