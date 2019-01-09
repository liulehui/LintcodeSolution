# coding:utf-8
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
# solution 1 recursion version
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.result = []
        if not root:
            return self.result
        
        self.traverse(root)
        return self.result
    
    def traverse(self,root):
        if not root:
            return
        self.traverse(root.left)
        self.result.append(root.val)
        self.traverse(root.right)
        
        return

# non recursion version 
class Solution2:
    def inorderTraversal(self,root):
        #result = []
        if not root:
            return []
        
        stack = []
        inorder = []
        node = root
        while node is not None:
            stack.append(node)
            node = node.left
        
        while stack:
            curt = stack.pop()
            inorder.append(curt.val)
            
            if curt.right:
                curt = curt.right 
                while curt:
                    stack.append(curt)
                    curt = curt.left
        return inorder 

