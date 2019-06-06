class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        
        from collections import deque
        
        queue = deque([])
        visited = set()
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    queue.append((i,j))
                    visited.add((i,j))
        print(visited)
        
        while queue:
            r, c = queue.popleft()
            print(r,c)
            board[r][c] = 'D'
            for delta_x,delta_y in self.directions:
                new_x = r + delta_x
                new_y = c + delta_y
                # visited.add((new_x,new_y))
                if self.is_valid_o(new_x,new_y,board):
                    queue.append((new_x,new_y))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "D":
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
        return 
    
    def is_valid_o(self,r,c,board):
        
        return r >=0 and r < len(board) and c >= 0 and c < len(board[0]) and board[r][c] == "O"