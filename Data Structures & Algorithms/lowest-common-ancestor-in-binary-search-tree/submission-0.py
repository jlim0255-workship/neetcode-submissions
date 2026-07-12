# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # this is a BST
        # p q are just for value to compare

        # naive
        # case 1: p and q are left and right of root
        # if (root.left == p.val and root.right == q.val) or (root.right == p.val and root.left == q.val):
        # case 2: p or q is root, the other is left or right (parent can be children too)

        # with BST property
        # all nodes in the left subtree are smaller than the node's value, vice versa for right
        # every subtrees also follow this property

        # iterative
        # curr = root
        # while curr:
        #     # if p and v both > curr value
        #     # p and q at the right subtree of curr
        #     if p.val > curr.val and q.val > curr.val:
        #         curr = curr.right

        #     elif p.val < curr.val and q.val < curr.val:
        #         curr = curr.left

        #     # at the middle
        #     # curr split p and q
        #     else:
        #         return curr

        # recursion
        if not root or not p or not q:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

        