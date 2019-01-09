"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

# divide and conquer
# here you need to have a result type to store whether there is A or B in the tree
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        find_A, find_B, lca = self.helper(root,A,B) 
        if find_A and find_B:
            return lca 
        else:
            return None 
    
    def helper(self,root,A,B):
        if root is None:
            return False,False,None 
        
        left_a, left_b, left_node = self.helper(root.left,A,B)
        right_a, right_b, right_node = self.helper(root.right,A,B) 
        
        a = left_a or right_a or root == A 
        # this means we can find a 
        b = left_b or right_b or root == B 
        # this means we can find b 
        
        if root == A or root == B:
            return a, b, root
        
        if left_node and right_node:
            return a, b, root
        
        if left_node:
            return a,b,left_node
        
        if right_node:
            return a, b, right_node
        
        return a,b,None 
