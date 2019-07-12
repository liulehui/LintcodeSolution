# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        node = root
        while root:
            if root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
        return node
        