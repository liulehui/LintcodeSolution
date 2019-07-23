"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# class Solution(object):
#     def preorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         result = []
#         self.helper(root,result)
#         return result
    
#     def helper(self,root,result):
#         if root is None:
#             return 
#         result.append(root.val)
#         for child in root.children:
#             self.helper(child,result)
        
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            
            stack.extend(root.children[::-1])
                
        return output       
