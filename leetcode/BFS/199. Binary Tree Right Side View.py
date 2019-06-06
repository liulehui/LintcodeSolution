# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None
        
        from collections import deque
        queue = deque([root])
        levels = []
        result = []
        while queue:
            level = []
            # print(len(queue))
            for i in range(len(queue)): 
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        result = [level[-1] for level in levels]
        return result
                