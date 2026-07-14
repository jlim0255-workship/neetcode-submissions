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

        # we need to bring down the root value down the traversal
        stack = [(root, root.val)]
        good_counter = 0

        while stack:
            node, current_max = stack.pop()

            # compare node.val with current max
            if node.val >= current_max:                
                good_counter += 1

            # update current max if node is bigger
            # this current_max will be overwritten as we going deeper down the tree
            # so the previously marked good node is preserved, as we adding new max
            current_max = max(node.val, current_max)

            # push the children into the stack with current max
            if node.left:
                stack.append((node.left, current_max))

            if node.right:
                stack.append((node.right, current_max))

        return good_counter