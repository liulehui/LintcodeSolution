# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self,isBST):
        self.isBST = isBST
        self.minNode = None
        self.maxNode = None 

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        return self.divideandconquer(root).isBST
        
    def divideandconquer(self, root):
        # write your code here
        # divide and conquer
        if not root:
            return ResultType(True)
      
        left = self.divideandconquer(root.left)
        right = self.divideandconquer(root.right)
        
        if left.isBST == False or right.isBST == False:
            return ResultType(False)
        
        if left.maxNode != None and left.maxNode.val >= root.val:
            return ResultType(False)
        
        if right.minNode != None and right.minNode.val <= root.val:
            return ResultType(False)
        
        result = ResultType(True)
        if left.minNode:
            result.minNode = left.minNode
        else:
            result.minNode = root
        if right.maxNode:
            result.maxNode = right.maxNode
        else:
            result.maxNode = root
    
        return result

# In order traverse, very easy       
class Solutions:
    # traverse
    def isValidBST(self,root):
        self.isBST = True
        self.lastVal = None 
        self.validate(root)
        return self.isBST
    
    def validate(self,root):
        if not root:
            return
        self.validate(root.left)
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return 
        self.lastVal = root.val 
        self.validate(root.right)