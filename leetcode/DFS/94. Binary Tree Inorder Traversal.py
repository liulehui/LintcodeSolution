class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.result = []
        self.helper(root)
        
        return self.result
    
    def helper(self,node):
        if not node:
            return 
        
        self.helper(node.left)
        self.result.append(node.val)
        self.helper(node.right)
        
        return 