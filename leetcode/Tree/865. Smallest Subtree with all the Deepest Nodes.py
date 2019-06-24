# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        result, dist = self.helper(root)
        return result
    
    def helper(self,root):
        if not root:
            return None, 0
        left_result, left_dist = self.helper(root.left)
        right_result, right_dist = self.helper(root.right)
        
        if left_dist > right_dist:
            return left_result, left_dist + 1
        if right_dist > left_dist:
            return right_result, right_dist + 1
        return root, left_dist + 1