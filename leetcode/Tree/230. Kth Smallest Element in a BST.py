# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        result = []
        if not root:
            return result
        
        def left_most(root):
            while root:
                self.stack.append(root)
                root = root.left
            
        left_most(root)
        
        while self.stack > 0:
            if len(result) >= k:
                return result[k-1]
            topmost_node = self.stack.pop()
            result.append(topmost_node.val)
            if topmost_node.right:
                left_most(topmost_node.right)
            else:
                continue
        
        