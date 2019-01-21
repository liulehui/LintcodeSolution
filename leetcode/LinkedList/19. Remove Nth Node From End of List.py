# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        p1,p2 = head,head
        k = n
        while k > 0:
            if p2.next == None:
                return head.next
            p2 = p2.next
            k -= 1
        
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        
        if n == 1:
            p1.next = None
        else:
            p1.next = p1.next.next
        return head
        
        
        