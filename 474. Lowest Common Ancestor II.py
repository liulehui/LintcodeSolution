"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        if not root:
            return None 
        
        if root == A or root == B:
            return root 
        
        parent_of_A = set()
        node = A 
        while node:
            parent_of_A.add(node)
            node = node.parent
        
        node = B 
        while node:
            if node in parent_of_A:
                return node 
            
            node = node.parent
        
        return None 
            
            
