# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def helper(root, curr, res, sum):
            if not root:
                return  # do nothing
            
            curr.append(root.val)
            if not root.left and not root.right: # leaf
                if root.val == sum:
                    res.append(curr[:]) # [:] to avoid aliasing
                curr.pop() # remove the leaf from curr after check
                
            else: # using else to avoid checking leaf's leaves.
                helper(root.left, curr, res, sum-root.val)
                helper(root.right, curr, res, sum-root.val)
                curr.pop() # remove the node from curr after check both its leaves

        curr, res = [], []
        helper(root, curr, res, sum)
        
        return res
        
        