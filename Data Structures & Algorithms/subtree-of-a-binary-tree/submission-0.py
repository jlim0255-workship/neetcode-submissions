# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.isSame(root, subRoot):
            return True

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
        
        return left and right