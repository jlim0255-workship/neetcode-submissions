# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs: stack

        # def dfs(p, q):
        #     # both of them null, same
        #     if not (p and q):
        #         return True

        #     # only one of them null, false
        #     if not p or not q:
        #         return False

        #     if p.val != q.val:
        #         return False            

        #     return dfs(p.left, q.left)

        # return dfs(p, q)

        # if not p and not q:
        #     return True

        # if not p or not q:
        #     return False

        # if p.val != q.val:
        #     return False

        # return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


        # if both trees run out at some point, meanign they are the same
        if not p and not q:
            return True

        # if one tree None and one tree not None, meaning they not the same
        if not p or not q:
            return False

        # if value not same, not same
        if p.val != q.val:
            return False

        # recursive case: go deeper for in each direction for each tree
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))


