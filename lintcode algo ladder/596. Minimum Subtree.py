# coding:utf-8
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        # post order traverse
        self.minimum = sys.maxsize
        self.result = None 
        self.helper(root)
        
        return self.result
    
    def helper(self,root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if left + right + root.val < self.minimum:
            self.minimum = left + right + root.val
            self.result = root 
        
        return left + right + root.val 