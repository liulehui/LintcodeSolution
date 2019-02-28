# coding:utf-8

# Solutions: 
# 使用单调栈，本质上找的是，以某个高度的bar为高度的最大矩阵面积
# 使用单调栈，找这个bar右边第一个比他小的bar
# 栈里前面那个数就是这个数左边第一个比他小的bar
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # mono stack
        heights.append(-1)
        
        stack = []
        # stack.append(0)
        
        result = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                # print(i)
                stack.append(i)
                i += 1
            else:
                num = stack.pop(-1)
                result = max(result,heights[num]*\
                             (i-stack[-1]-1 if stack else i))
        return result
            
            