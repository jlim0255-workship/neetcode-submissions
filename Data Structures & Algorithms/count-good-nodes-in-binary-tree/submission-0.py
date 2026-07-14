# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # naive
        # dfs
        # stack = [root]

        # good_counter = 0

        # while stack:
        #     node = stack.pop()

        #     if node.left:
        #         stack.append(node.left)

        #         # check left and right children of node
        #         # increment if left child is greater than parent
        #         if node.left.val >= node.val:
        #             good_counter += 1

        #     if node.right:
        #         stack.append(node.right)

        #         # increment if right child is greater than parent
        #         if node.right.val >= node.val:
        #             good_counter += 1

        # return good_counter

        stack = [(root, root.val)]
        good_counter = 0

        while stack:
            node, current_max = stack.pop()

            if node.val >= current_max:                
                good_counter += 1

            # update current max
            current_max = max(node.val, current_max)

            if node.left:
                stack.append((node.left, current_max))

            if node.right:
                stack.append((node.right, current_max))

        return good_counter