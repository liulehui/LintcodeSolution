class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        if n <= 0:
            return 0
        
        self.result = 0
        cols = {}
        self.search(0,cols,n)
        
        return self.result
    
    def search(self,row,cols,n):
        if row == n:
            self.result += 1
            return 
        
        for col in range(n):
            if col in cols:
                continue
            if self.attack(row,col,cols):
                continue
            
            cols[col] = row
            self.search(row+1,cols,n)
            del cols[col]
        
    def attack(self,row,col,cols):
        for c,r in cols.items():
            if c - r == col - row or c + r == col + row:
                return True
        
        return False