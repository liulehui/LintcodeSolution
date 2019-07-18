# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next is not None and head.next.next is not None:
            n1, n2 = head.next, head.next.next
            # head -> n1 -> n2
            # head -> n2 -> n1
            head.next = n2
            n1.next = n2.next
            n2.next = n1
            
            head = n1
        return dummy.next
        