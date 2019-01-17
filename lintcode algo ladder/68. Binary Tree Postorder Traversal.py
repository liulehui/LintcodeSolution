# coding:utf-8
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 这题有点绕，看答案有人说可以用morris算法
# 这里用的是用一个prev记录上一次访问过的点，然后看栈顶的node,如果有左儿子，就push进栈
# 这样一路push可以找到最左边的那个node,只要满足当前这个点prev是自己，且上个访问过的节点不是自己的
# 左儿子，那就可以append到result里，如果是的话说明是现在访问的node是已经访问过的
# 就看有没有右儿子
# 有的话继续，没有的话这个也append到result，完成post traversal

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        stack = []
        postorder = []
        prev = None # previously traversed node
        curr = root
        stack.append(root)
        while stack:
            curr = stack[-1]
            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left is not None:
                    stack.append(curr.left)
                elif curr.right is not None:
                    stack.append(curr.right)
            else:
                if curr.left == prev:
                    if curr.right is not None:
                        stack.append(curr.right)
                else:
                    postorder.append(curr.val)
                    stack.pop()
            prev = curr
            
        return postorder
            
            
                
