# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the list to 
        # [0, n-1, 1, n-2, 2, ...]

        # fast and slow pointers
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # the start of second half
        second = slow.next

        # reverse second half        
        prev = slow.next = None
        while second:
            tmp = second.next

            second.next = prev

            prev = second

            second = tmp
        
        # merge 2 halves
        # new head of the second (at the right)
        second = prev

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second

            second.next = tmp1
        
            first = tmp1
            second = tmp2






        # keep going until fast pointer reach None or last value of the list

        # if even number of node
        # slow.next = start of right list

        # if odd number of node
        # slow.next


