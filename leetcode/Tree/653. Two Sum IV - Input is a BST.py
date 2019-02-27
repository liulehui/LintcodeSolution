# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        result = []
        self.traverse(root,result)
        
        l, r = 0, len(result) -1 
        
        while l < r:
            if result[l] + result[r] == k:
                return True
            elif result[l] + result[r] < k:
                l += 1
            else:
                r -= 1
        
        return False
    
    def traverse(self,root,result):
        if root == None:
            return
        self.traverse(root.left,result)
        result.append(root.val)
        self.traverse(root.right,result)
        return 
        