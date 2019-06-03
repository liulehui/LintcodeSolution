"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # inorder traverse
        # O(n) space: inorder traverse append to a list then combine
        self.last, self.first = None, None
        
        def helper(node):
            
            if node:
                # helper
                helper(node.left)
                
                if self.last:
                    self.last.right = node
                    node.left = self.last
                else:
                    self.first = node
                
                self.last = node
                
                # right
                helper(node.right)
                
        if not root:
            return None
        
        # the smallest first and the largest node
        helper(root)
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first
                
                
        