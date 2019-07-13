class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left + 1 < right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n
            mid_val = matrix[x][y]
            if target == mid_val:
                return True
            else:
                if target < mid_val:
                    right = mid
                else:
                    left = mid
        if matrix[left // n][left % n] == target:
            return True
        if matrix[right // n][right % n] == target:
            return True
        return False
        
        