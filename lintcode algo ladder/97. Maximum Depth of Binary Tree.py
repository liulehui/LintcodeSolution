# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# when it comes to binary tree, think about the divide and conquer
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        depth = 0 
        if not root:
            return depth
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1 