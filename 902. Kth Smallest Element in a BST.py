# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# BST of inorder traverse, the kth is just the Kth node in the traverse
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        stack = []
        
        while root:
            stack.append(root)
            root = root.left
        
        count = k - 1 
        print(count)
        while stack:
            curr = stack.pop()
            print(curr.val)
            if count == 0:
                return curr.val 
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left 
            count -= 1 
            
            
                
