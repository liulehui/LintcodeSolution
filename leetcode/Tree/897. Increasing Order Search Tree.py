# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
    
        self.inorder = []
        self.helper(root)
        
        new_head = new_tail = TreeNode(None)
        for node in self.inorder:
            node = TreeNode(node.val)
            new_tail.right = node
            new_tail.left = None
            new_tail = new_tail.right
        
        return new_head.right
    def helper(self,node):
        if node is None:
            return
        self.helper(node.left)
        self.inorder.append(node)
        self.helper(node.right)
        return 