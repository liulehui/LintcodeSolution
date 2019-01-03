class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    # BFS 搜索，看到有1的就搜索之，然后把和他相邻的都变成0
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.bfs(grid,i,j)
                    count += 1 
        
        return count
    
    def bfs(self,grid,x,y):
        queue = collections.deque([(x,y)])
        grid[x][y] = 0
        while queue:
            x, y = queue.popleft()
            delta_grid = [(0,1),(1,0),(-1,0),(0,-1)]
            for delta_x,delta_y in delta_grid:
                next_x = x+delta_x
                next_y = y+delta_y
                if not self.is_valid(grid,next_x,next_y):
                    continue
                queue.append((next_x,next_y))
                grid[next_x][next_y] = 0
    
    def is_valid(self,grid,x,y):
        return x>=0 and  x<len(grid) and y>=0 and y < len(grid[0]) and grid[x][y]
                
