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
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n_row, n_col = len(matrix), len(matrix[0])
        heights = [0 for j in matrix[0]]
        result = 0
        for i in range(n_row):
            for j in range(n_col):
                if int(matrix[i][j]) == 0:
                    heights[j] = 0
                else:
                    heights[j] += int(matrix[i][j])
            result = max(self.largestRectangleArea(heights),result)
        
        return result
        