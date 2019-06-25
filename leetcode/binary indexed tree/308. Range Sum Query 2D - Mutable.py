class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if not matrix or not matrix[0]:
            return None
        self.m, self.n = len(matrix), len(matrix[0])
        self.bit = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.add(i,j,self.matrix[i][j])
    
    def lowbit(self,x):
        return x & (-x)
    
    def add(self,i,j,val):
        # i += 1
        # j += 1
        xi = i + 1
        while xi <= self.m:
            yi = j + 1
            while yi <= self.n:
                self.bit[xi][yi] += val
                yi += self.lowbit(yi)
            xi += self.lowbit(xi)
    
    def sum(self,i,j):
        xi = i + 1
        # yi = j + 1
        res = 0
        
        while xi > 0:
            yi = j + 1
            while yi > 0:
                res += self.bit[xi][yi]
                yi -= self.lowbit(yi)
            xi -= self.lowbit(xi)
        return res
    
    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        self.add(row,col,val - self.matrix[row][col])
        self.matrix[row][col] = val
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum(row2,col2) - self.sum(row1 - 1,col2) - self.sum(row2,col1-1) + self.sum(row1-1,col1-1)
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)