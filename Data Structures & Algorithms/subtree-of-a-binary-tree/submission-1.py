# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # MEAT: empty Tree is a subTree of every tree
        if not subRoot:
            return True

        # if no root at all, false
        if not root:
            return False

        # the first pass in and both match
        if self.isSame(root, subRoot):
            return True
        
        # other rounds
        # MEAT: pass in root left right, and the WHOLE subRoot (not subRoot left and right)
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def isSame(self, r, sr):
        if not r and not sr:
            return True

        if not r or not sr:
            return False

        if r.val != sr.val:
            return False

        left = self.isSame(r.left, sr.left)
        right = self.isSame(r.right, sr.right)
        
        return left and right # only True if left and right branch identical