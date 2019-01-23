# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
            
        while l1:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        
        while l2:
            tail.next = l2
            tail = tail.next
            l2 = l2.next
        
        return dummy.next