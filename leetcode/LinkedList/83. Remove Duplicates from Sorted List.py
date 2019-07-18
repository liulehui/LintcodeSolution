# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        if not head.next:
            return head
        
        node = head
        while node and node.next:
            while node and node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
            
        return head
            