# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stack = []
        def push_stack(root):
            while root:
                stack.append(root)
                root = root.left
        push_stack(root)
        new_root = new_leaf = stack.pop()
        new_leaf.left = None
        
        while len(stack) > 0:
            # print(len(stack))
            node = stack.pop()
            if node.right:
                push_stack(node.right)
            
            new_leaf.right = node
            new_leaf.left = None
            new_leaf = new_leaf.right
            
        return new_root
