# coding:utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
        n = len(matrix)
        # first do the transpose
        for r in range(n):
            for c in range(r,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
                
        # second flip horizotally
        for r in range(n):
            for c in range(0,n//2):
                matrix[r][c], matrix[r][n-1-c] = matrix[r][n-1-c], matrix[r][c]
        
        # print(matrix)
        return