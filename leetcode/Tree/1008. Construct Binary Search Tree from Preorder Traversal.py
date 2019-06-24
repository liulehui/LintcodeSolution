class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or len(preorder) == 0:
            return None
        self.preorder = preorder
        self.index = 0
        self.n = len(preorder)
        return self.helper()
    
    def helper(self,lower = float("-inf"),upper = float('inf')):
        if self.index == self.n:
            return None
        val = self.preorder[self.index]
        
        if val < lower or val > upper:
            return None
        
        self.index += 1
        root = TreeNode(val)
        root.left = self.helper(lower,val)
        root.right = self.helper(val,upper)
        
        return root