# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # if not bst mentioned, we can use sliding window?
        # how many steps from root?
        # dfs in order, left root right, guaranteed ascending order

        # init a counter, to keep track the kth smallest
        # run a counter inside the loop, if both matches, meaning we can return that node val
        stack = []
        counter = 0 
        curr = root       

        while stack or curr:
            
            # reach the leftmost node of current node
            while curr:                
                stack.append(curr)
                curr = curr.left                

            # backtrack, get the leftmost node out, middle node, right node
            curr = stack.pop()
            counter += 1

            if counter == k:
                return curr.val                    

            curr = curr.right

            
            



        
