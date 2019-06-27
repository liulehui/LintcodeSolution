# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
# 
class Solution:
    last_node = None
    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    
    def helper(self,root):
        if not root:
            return None
        
        # return the last value of the flatten tree
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        if right_last:
            return right_last
        
        if left_last:
            return left_last
        
        return root
            
        
            
            
            