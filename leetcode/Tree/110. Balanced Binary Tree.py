# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True
#         left_height = self.height(root.left)
        
#         right_height = self.height(root.right)
        
#         return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
#     def height(self,root):
#         if not root:
#             return 0
#         return max(self.height(root.left),self.height(root.right)) + 1

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced
        
    def validate(self, root):
        if root is None:
            return True, 0
            
        balanced, leftHeight = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, rightHeight = self.validate(root.right)
        if not balanced:
            return False, 0
            
        return abs(leftHeight - rightHeight) <= 1, max(leftHeight, rightHeight) + 1