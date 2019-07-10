# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Result Type的思想，返回两个值
# 以root为节点的maxSum 和 从这个root出发的最长pathSum
# maxSum 有两种，一种是不经过root的左子树的maxSum或右子树的maxSum 
# 另一种是经过root， 左边最大 + root + 右边最大。
# recursion的返回比较tricky， 为了不干扰，root为None时，maxSum = 负无穷， pathSum = 0
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        maxSum, _ = self.maxPathHelper(root)
        return maxSum
        
    def maxPathHelper(self, root):
        if root is None:
            return -sys.maxint, 0
        
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)
        
        return maxpath, single

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # time O(N) space O(h)
        self.max_sum = float('-inf')
        self.max_gain(root)
        return self.max_sum
    
    def max_gain(self,node):
        if not node:
            return 0

        # max sum on the left and right sub-trees of node
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        self.max_sum = max(self.max_sum, price_newpath)

        # for recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)
        