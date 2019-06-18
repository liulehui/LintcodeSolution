# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        # bfs should do 
        
        self.result = float("inf")
        min1 = root.val
        
        def dfs(node):
            if node:
                if min1 < node.val < self.result:
                    self.result = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.result if self.result < float("inf") else -1
        
        
            
        
        