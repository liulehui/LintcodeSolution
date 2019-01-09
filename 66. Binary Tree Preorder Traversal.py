"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        self.result = []
        if not root:
            return self.result
        self.traverse(root)
        return self.result
    
    def traverse(self,root):
        if root is None:
            return 
        self.result.append(root.val)
        
        self.traverse(root.left)
        self.traverse(root.right)
    
    
        
