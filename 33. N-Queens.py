# coding:utf-8
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        results = []
        if n <= 0:
            return results
        self.search(results,[],n)
        return results
    
    def search(self,results,cols,n):
        row = len(cols) 
        # len(cols) 表示已经放了几个Q
        # 然后因为row是从0开始的，所以可以认为现在要放
        # 第row行这个Q
        if row == n:
            results.append(self.draw_chessboard(cols))
            return 
        # 这里遍历0-n-1个列 看可不可以放进去
        for col in range(0,n):
            if not self.is_valid(cols,row,col):
                continue
            cols.append(col)
            self.search(results,cols,n)
            cols.pop()
            
    def draw_chessboard(self,cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board 
    
    def is_valid(self,cols,row,col):
        for r,c in enumerate(cols):
            if c == col:
                return False
            if r - c == row - col:
                return False
            if r + c == row + col:
                return False
        
        return True