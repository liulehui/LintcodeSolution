# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if not root:
#             return None
        
#         if root == p or root == q:
#             return root
        
#         left = self.lowestCommonAncestor(root.left,p,q)
#         right = self.lowestCommonAncestor(root.right,p,q)
#         # if left not null
#         if left is not None and right is not None:
#             return root
#         if right != None:
#             return right
#         if left != None:
#             return left
        
#         return None

# use the characteristic of bst
class Solution(object):
    def lowestCommonAncestor(self,root,p,q):
        if not root:
            return None
        if root == p or root == q:
            return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        return root
        
        