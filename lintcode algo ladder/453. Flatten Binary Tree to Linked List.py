# coding:utf-8
# divide and conquer
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.helper(root)
        
    def helper(self,root):
        if not root:
            return None 
        
        left_last = self.helper(root.left)
        right_last = self.helper(root.right)
        
        # concaten left to right 
        if left_last:
            
            left_last.right = root.right
            root.right = root.left 
            root.left = None 
        
        if right_last:
            return right_last
            
        if left_last:
            return left_last
        return root

# traverse
class Solution2:
    last_node = None
    
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if root is None:
            return
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = root
            
        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)