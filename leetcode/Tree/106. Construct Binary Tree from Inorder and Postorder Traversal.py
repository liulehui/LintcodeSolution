# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        rootIdx = inorder.index(postorder[-1])
        
        # left_length = rootIdx
        root.left = self.buildTree(inorder[:rootIdx], postorder[:rootIdx])
        root.right = self.buildTree(inorder[rootIdx+1:], postorder[rootIdx:-1])
        return root
        