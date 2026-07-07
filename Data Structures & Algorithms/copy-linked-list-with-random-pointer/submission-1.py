"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 2 passes
        oldToCopy = {None: None}

        
        # 1 pass: to create deep copy of nodes, create hash map, old node to new copy
        cur = head
        while cur:
            copy = Node(cur.val, cur.next, cur.random)
            oldToCopy[cur] =  copy
            cur = cur.next

        # 2nd pass: pointers

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next


        # return the dict[head]
        return oldToCopy[head]
