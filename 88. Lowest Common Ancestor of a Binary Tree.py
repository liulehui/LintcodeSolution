# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# divide and conquer
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        
        # there are some situations:
        # A and B in the below tree ===> A 
        # B and A in the below tree ===> B 
        # A and B in different tree ===> root 
        # 
        if root is None:
            return None 
        
        if root == A or root == B:
            return root
        
        left_result = self.lowestCommonAncestor(root.left,A,B)
        right_result = self.lowestCommonAncestor(root.right,A,B)
        
        if left_result and right_result:
            return root 
        if left_result:
            return left_result
        if right_result:
            return right_result
        
        return None 
        
