# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "{}"
        from collections import deque
        queue = deque([root])
        
        level = [root]
        result = [root.val]
        
        while level:
            new_level = []
            for node in level:
                if node.left:
                    result.extend([node.left.val])
                    new_level.append(node.left)
                else:
                    result.extend("#")
                    
                if node.right:
                    result.extend([node.right.val])
                    new_level.append(node.right)
                else:
                    result.extend("#")
            
            level = new_level
            
        while result and result[-1] == "#":
            result.pop()
        
        return '{' + ','.join(map(str, result)) + '}' 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "{}":
            return 
        
        nodes = collections.deque([TreeNode(n) for n in data[1:-1].split(',')])
        root = nodes.popleft()
        level = [root]
        while level:
            new_level = []
            for n in level:
                if nodes:
                    left_node = nodes.popleft()
                    if left_node.val != '#':
                        n.left = left_node
                        new_level.append(n.left)
                    else:
                        n.left = None
                    
                    # print('left node')
                    # print(n.left)

                if nodes:
                    right_node = nodes.popleft()
                    if right_node.val != '#':
                        n.right = right_node
                        new_level.append(n.right)
                    else:
                        n.right = None
                    # print('right node')
                    # print(n.right)    
                    
            level = new_level 

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))