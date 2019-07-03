# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution(object):
#     cnt=0
#     def pathSum(self, root, sum):
#         """
#         :type root: TreeNode
#         :type sum: int
#         :rtype: int
#         """
#         if root==None:
#             return 0
#         self.path(root,sum)
#         self.pathSum(root.left,sum)
#         self.pathSum(root.right,sum)
#         return self.cnt
        
#     def path(self,root,sum):
#         if root==None:
#             return
#         if root.val==sum:
#             self.cnt+=1
#         self.path(root.left,sum-root.val)
#         self.path(root.right,sum-root.val)
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # 返回 dict记录到当前节点结束的路径的的和，那么以curSum和sum之间如果前面有过，就+几
        def dfs(node, curSum):
            self.count += d[curSum - sum]
            d[curSum] += 1
            if node.left: dfs(node.left, curSum + node.left.val)
            if node.right: dfs(node.right, curSum + node.right.val)
            d[curSum] -= 1
            
        self.count = 0
        d = collections.defaultdict(int)
        d[0] = 1
        if root: dfs(root, root.val)
        return self.count