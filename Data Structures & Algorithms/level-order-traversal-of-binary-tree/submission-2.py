# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root is None:
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            # how far is this level from root ndoe?
            level = len(queue)
            
            # all nodes in this level
            current_level_values = []

            # relax the node, add in neighbors
            for _ in range(level):
                node = queue.popleft()
                current_level_values.append(node.val)

                # extend the queue children of this node in this level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # after this, append the whole level
            res.append(current_level_values)

        return res

        # this is dfs btw also works
        # final_res = []
        # def _traverse(node, level, res):
        #     if not node:
        #         return 

        #     if level == len(res):
        #         res.append([])

        #     res[level].append(node.val)
        
        #     # go left
        #     _traverse(node.left, level + 1, res)            

        #     # go right
        #     _traverse(node.right, level + 1, res)

        # _traverse(root, 0, final_res)

        # return final_res