"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return 0
        
        lower_node = self.lowerbound(root,target)
        higher_node = self.higherbound(root,target)
        
        if lower_node is None:
            return higher_node.val 
        
        if higher_node is None:
            return lower_node.val 
        
        if ( target - lower_node.val ) > ( higher_node.val - target ):
            return higher_node.val 
        else:
            return lower_node.val 
    
    def lowerbound(self,root,target):
        if not root:
            return 
        if target <= root.val:
            return self.lowerbound(root.left,target)
        
        # if target > root.val 
        right_node = self.lowerbound(root.right,target)
        if right_node:
            return right_node 
        else:
            return root 
    
    def higherbound(self,root,target):
        if not root:
            return 
        if target >= root.val:
            return self.higherbound(root.right,target)
        
        # if target < root.val 
        left_node = self.higherbound(root.left,target)
        if left_node:
            return left_node 
        else:
            return root