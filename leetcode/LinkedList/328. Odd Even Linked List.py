# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_odd = ListNode(0)
        dummy_even = ListNode(0)
        p1 = dummy_odd
        p2 = dummy_even
        p3 = head
        
        while p3 is not None and p3.next is not None:
            p1.next = p3
            p1 = p1.next
            p2.next = p3.next
            p2 = p2.next
            p3 = p3.next.next
        
        if p3 is None:
            # append even to odd
            p2.next = None
            p1.next = dummy_even.next
        else:
            # append p3 to odd then append even to odd
            p1.next = p3
            p1 = p1.next
            p2.next = None
            p1.next = dummy_even.next
        
        return dummy_odd.next
        
        