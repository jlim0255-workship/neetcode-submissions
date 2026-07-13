# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # if root is None:
        # if not root:
        #     return []

        # queue = deque([root])
        # res = []

        # while queue:
        #     level = len(queue)
            
        #     current_level_values = []

        #     # relax the node
        #     for _ in range(level):
        #         node = queue.popleft()
        #         current_level_values.append(node.val)

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)

        #     res.append(current_level_values)

        # return res

        # this is dfs btw
        final_res = []
        def _traverse(node, level, res):
            if not node:
                return 

            if level == len(res):
                res.append([])

            res[level].append(node.val)
        
            # go left
            _traverse(node.left, level + 1, res)            

            # go right
            _traverse(node.right, level + 1, res)

        _traverse(root, 0, final_res)

        return final_res

