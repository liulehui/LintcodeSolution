# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
# class Solution:
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         else:
#             node_deque = deque([(1, root),])
        
#         while node_deque:
#             depth, root = node_deque.popleft()
#             print(depth,root)
#             children = [root.left, root.right]
#             print(children)
#             if not any(children):
#                 return depth
#             for c in children:
#                 if c:
#                     node_deque.append((depth + 1, c))
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        from collections import deque
        result = 0
        queue = deque([root])
        while queue:
            result += 1
            for i in range(len(queue)):
                # print(i)
                node = queue.popleft()
                # print(node.val)
                if (node.left is None) and (node.right is None):
                    return result
                # print(node.left.val,node.right.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return result