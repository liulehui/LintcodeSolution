"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        
        node = Node(insertVal,head)
        val = insertVal
        
        if not head:
            return node
        
        prev, cur = head, head.next
        while True:
            if prev.val <= val <= cur.val:
                break
            elif prev.val > cur.val and (val < cur.val or val > prev.val):
                break
            prev, cur = prev.next, cur.next
            if prev == head:
                break
        
        prev.next = node
        node.next = cur
        return head
        
        
        
        