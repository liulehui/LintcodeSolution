# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_height = self.height(root.left)
        
        right_height = self.height(root.right)
        
        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1