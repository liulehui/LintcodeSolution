# coding:utf-8
class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    def maxSubmatrix(self, matrix):
        # write your code here
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return 0
        
        # calculate prefix sum between row and row
        pre_sum = self.get_prefixsum(matrix,m,n)
        
        max_sum = -sys.maxsize
        
        for up in range(m):
            for down in range(up,m):
                arr = self.compress(matrix,up,down,pre_sum,n)
                max_sum = max(max_sum,self.maximum_subarray(arr))
        return max_sum
    
    def get_prefixsum(self,matrix,row,col):
        sum = [[0 for i in range(col)] for j in range(row+1)]
        
        for i in range(row):
            for j in range(col):
                sum[i+1][j] = sum[i][j] + matrix[i][j] 
        
        return sum 
    
    def compress(self,matix,up,down,prefix_sum,col):
        arr = [0 for i in range(col)]
        for i in range(col):
            arr[i] = prefix_sum[down+1][i] - prefix_sum[up][i]
        
        return arr 
    
    def maximum_subarray(self,arr):
        temp_max = -sys.maxsize
        temp_min = 0
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            temp_max = max(temp_max,sum-temp_min)
            temp_min = min(temp_min,sum)
            
        return temp_max
        