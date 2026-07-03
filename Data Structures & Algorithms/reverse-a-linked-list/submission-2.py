# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stack implementation
        # # if head is None
        # if not head:
        #     return None

        # # use stack
        # stack = []
        # temp = head        

        # # keep appending the elements into the stack, except for the last element (its next != None)
        # while temp.next is not None:
        #     stack.append(temp)

        #     # update to the next 
        #     temp = temp.next

        # # temp and head must be the same 
        # head = temp

        # while stack:
        #     temp.next = stack.pop()
        #     temp = temp.next

        # temp.next = None

        # return head

        # iteration implementation (the normal pointer way)
        if not head:
            return None

        prev = None
        nextNode = None
        curr = head

        # while curr.next is not None:
        while curr is not None:
            nextNode = curr.next

            curr.next = prev
            # prev = curr.next

            prev = curr
            curr = nextNode

        return prev
        # prev, curr = None, head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev


        