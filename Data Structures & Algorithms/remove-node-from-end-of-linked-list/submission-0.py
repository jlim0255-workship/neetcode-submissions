# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init dummy node
        dummy = ListNode(0, head)

        # fast is at head, slow at dummy node
        slow = dummy
        fast = head

        while n > 0:
            # advance fast pointer N step ahead slow
            fast = fast.next
            n -= 1
        
        # move fast to None, so slow will land on the node to be deleted
        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow now land on the node to be deleted
        # adjust the next link
        slow.next = slow.next.next

        return dummy.next


