# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = node = ListNode(0)
        # carry = 0
                
        # # first reverse the list
        # prev1 = None
        # next1 = None
        # prev2 = None
        # next2 = None
                
        # while l1:
        #     next1 = l1.next

        #     l1.next = prev1

        #     prev1 = l1

        #     l1 = next1

        # while l2:
        #     # assign next value
        #     next2 = l2.next

        #     # curr pointer points to prev
        #     l2.next = prev2

        #     # move prev left
        #     prev2 = l2

        #     # move curr left
        #     l2 = next2

        # # head at prev1 and prev2
        # carry = 0

        # # do the sum
        # while prev1 and prev2:
        #     the_sum = prev1.val + prev2.val + carry
        #     newNode = ListNode()

        #     if the_sum >= 10:
        #         carry = 1        
        #         newNode.val = the_sum - 10

        #     else:
        #         carry = 0
        #         newNode.val = the_sum

        #     # points to the newNode
        #     node.next = newNode

        #     # advance the node
        #     node = node.next
            
        #     prev1 = prev1.next
        #     prev2 = prev2.next

        # # the leftovers, still can do a carry
        # if prev1 or prev2:

        #     if prev1 is None:
        #         newNode = ListNode()
        #         the_sum = prev2.val + carry
        #         if the_sum >= 10:
        #             newNode.val = the_sum - 10
                    
        #             # points to the next place
        #             node.next = newNode

        #             # add the carry
        #             carryNode = ListNode()
        #             carryNode.val = 1
        #             node.next = carryNode
                
        #         else:
        #             newNode.val = the_sum
                    
        #             # points to the next place
        #             node.next = newNode

                
        #         node.next = prev2
        #         node = node.next

        #     else:
        #         newNode = ListNode()
        #         the_sum = prev1.val + carry
        #         if the_sum >= 10:
        #             newNode.val = the_sum - 10
                    
        #             # points to the next place
        #             node.next = newNode

        #             # advance node
        #             node = node.next

        #             # add the carry
        #             carryNode = ListNode()
        #             carryNode.val = 1
        #             node.next = carryNode
                    
        #         else:
        #             newNode.val = the_sum
                    
        #             # points to the next place
        #             node.next = newNode

        #         node.next = prev1
        #         node = node.next


        # # reverse the node again?


        # return dummy.next

        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10

            val = val % 10

            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None

            l2 = l2.next if l2 else None

        return dummy.next


