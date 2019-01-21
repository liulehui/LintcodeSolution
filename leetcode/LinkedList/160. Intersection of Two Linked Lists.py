# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p_a = headA
        p_b = headB
        if p_a is None or p_b is None:
            return False
        
        while p_a != p_b:
            if p_a is not None:
                p_a = p_a.next
            else:
                p_a = headB
            if p_b is not None:
                p_b = p_b.next
            else:
                p_b = headA
        return p_a
            
            
            
        