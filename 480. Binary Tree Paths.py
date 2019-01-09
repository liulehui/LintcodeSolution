class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        
        result = []
        
        if not root:
            return result
        
        path = []  
        self.helper(root,path,result)
        return result
    
    def helper(self,node,path,result):
        path.append(str(node.val))
        
        if node.left is None and node.right is None:
            result.append('->'.join(path))
            path.pop()
            return
        
        if node.left:
            self.helper(node.left,path,result)
        
        if node.right:
            self.helper(node.right,path,result)
        
        path.pop()

class Solution2:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if root is None:
            return []
            
        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + '->' + path)
        
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + '->' + path)
            
        return paths
        