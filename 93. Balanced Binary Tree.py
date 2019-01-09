# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self,depth,isBalanced):
        self.depth = depth
        self.isBalanced = isBalanced
        
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        
        return self.maxdepth(root).isBalanced
    
    def maxdepth(self,root):
        if not root:
            return ResultType(0,True)
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        
        max_depth = max(left.depth,right.depth) + 1 
        
        
        if not left.isBalanced or not right.isBalanced:
            return ResultType(max_depth,False)
        if abs(left.depth-right.depth) > 1:
            return ResultType(max_depth,False)
        return ResultType(max_depth,True)
        
