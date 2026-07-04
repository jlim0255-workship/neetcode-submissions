# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check the len of both lists
        dummy = node = ListNode()

        # set the pointer on list 1 and 2
        while list1 and list2:
            # if list1 smaller
            if list1.val < list2.val:

                # point the node next to list1
                node.next = list1

                # advance list1
                list1 = list1.next

            # list2 smaller
            else:
                # point the node next to list2
                node.next = list2

                # advance list2
                list2 = list2.next

            # advance the node next pointer
            node = node.next

        # either list 1 or 2 will run out
        # point the next pointer to the remaining list
        if list1 is None:
            node.next = list2

        else:
            node.next = list1

        # MEAT: the next value is the head, dummy is the Node !
        return dummy.next