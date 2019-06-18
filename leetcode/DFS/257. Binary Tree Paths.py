# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.paths = []
        self.helper(root,[str(root.val)])
        return self.paths
        
    def helper(self,root,path):
        if not root.left and not root.right:
            self.paths.append("->".join(path))
            return 
        if root.left:
            path.append(str(root.left.val))
            self.helper(root.left,path)
            path.pop()
            
        if root.right:
            path.append(str(root.right.val))
            self.helper(root.right,path)
            path.pop()
        
                