# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque([root])
        res = []

        # if no right node, get left node        
        while queue:
            # level
            level = len(queue)

            # set a last node variable to be overwritten at every level
            rightmostNode = None

            # go through every node in this level
            for _ in range(len(queue)):
                # get only the right most node of this level
                node = queue.popleft()
                rightmostNode = node

                # append queue with the right only
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(rightmostNode.val)

        return res