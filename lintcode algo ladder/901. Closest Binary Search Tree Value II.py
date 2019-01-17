# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# brute force algorithm 
# inorder traverse find the first index that the element >= target
# use two pointer algo to find the kth closest value 

# algo 2 use two stack, need further listen to lecture
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        self.inorder = []
        self.traverse(root,self.inorder)
       
        # binary search to find the first element greater than target
        start = 0
        end = len(self.inorder) - 1 
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            
            if self.inorder[mid] < target:
                start = mid 
            else:
                end = mid 
        
        index = 0
        if self.inorder[end] <= target:
            index = end
        else:
            index = start
        left = index 
        right = index + 1 # this is the index of the first element > target
        
       
        ans = []
        while len(ans) < k:
            if self.isLeftCloser(left,right,target):
                ans.append(self.inorder[left])
                left -= 1 
            else:
                ans.append(self.inorder[right])
                right += 1 
        
        return ans 
    
    def traverse(self,root,inorder):
        if root is None:
            return 
        self.traverse(root.left,inorder)
        inorder.append(root.val)
        self.traverse(root.right,inorder)
        return 
    
    def isLeftCloser(self,left,right,target):
        if left < 0:
            return False
        if right > len(self.inorder) - 1:
            return True
        if abs(self.inorder[left]-target) <= abs(self.inorder[right] - target):
            return True
        else:
            return False
        