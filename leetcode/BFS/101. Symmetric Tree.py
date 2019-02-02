# coding:utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Solution 1 : use a queue and 
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         # level traverse and each level should be sysmetric
        
#         if root is None:
#             return True
        
#         from collections import deque
        
#         queue = deque([root,root])
        
#         while queue:
#             node_1 = queue.popleft()
#             node_2 = queue.popleft()
            
#             if node_1 is None and node_2 is None:
#                 continue
#             if node_1 is None or node_2 is None:
#                 return False
#             if node_1.val != node_2.val:
#                 return False
#             queue.append(node_1.left)
#             queue.append(node_2.right)
#             queue.append(node_1.right)
#             queue.append(node_2.left)
        
#         return True
# Solutions 2
class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root,root)
    def isMirror(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)