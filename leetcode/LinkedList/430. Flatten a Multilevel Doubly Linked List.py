# coding:utf-8
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return head 
        
        p = head
        while p != None:
            if p.child == None:
                p = p.next
                continue
            
            temp = p.child
            # find the tail of temp and connect it to p.next
            while temp.next is not None:
                temp = temp.next
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp
            
            # then append p to p.child
            p.next = p.child
            p.child.prev = p
            p.child = None
        return head