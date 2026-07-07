# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the list to 
        # [0, n-1, 1, n-2, 2, ...]
        # use this example input
        # [1, 2, 3, 4, 5]

        # fast and slow pointers
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # the start of second half 
        second = slow.next # second = 3.next = 4

        # reverse second half        
        # prev = slow.next = None # Python evaluates right to left
        
        slow.next = None # now slow.next is None, first half, start = head, end = None
        
        prev = None # for reversal, tracking the most recent reversed node

        while second:
            # save the next node
            tmp = second.next # 4.next = 5 # tmp = 5.next = None

            # flip current node backward
            second.next = prev # 4.next now points to prev, prev = None # second.next = 5.next now points to 4

            # shift prev forward 
            prev = second # prev = 4 # prev = 5

            # shift second forward
            second = tmp # second = tmp = 5 # second = tmp = None
        
        # merge 2 halves
        # new head of the second (at the right)
        second = prev

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second # first.next points to the end

            second.next = tmp1 # second.next points to the first
        
            first = tmp1 # first was 1, now 2
            second = tmp2 # second was 5, now 4
