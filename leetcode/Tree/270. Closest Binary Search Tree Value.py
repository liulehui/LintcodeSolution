# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        
        close_val = root.val
        
        while root:
			# store the closest root value
            if abs(root.val - target) < abs(close_val - target):
                close_val = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return close_val