"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        # x,y = source.x,source.y
        # if source.x == destination.x and source.y == destination.y:
         #   return 0
        count = -1
        queue = collections.deque()
        queue.append((source.x,source.y))
        
        delta_grid = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        dis_hash = {(source.x,source.y):0}
        
        while queue:
            x,y = queue.popleft()
            if (x, y) == (destination.x, destination.y):
                return dis_hash[(x, y)]

            for delta_x,delta_y in delta_grid:
                next_x = x + delta_x
                next_y = y + delta_y
                if (next_x,next_y) in dis_hash:
                    continue
                if not self.is_valid(grid,next_x,next_y):
                    continue
                dis_hash[(next_x, next_y)] = dis_hash[(x, y)] + 1
                queue.append((next_x,next_y))
        return -1
            
    def is_valid(self,grid,x,y):
        return x>=0 and x< len(grid) and y>=0 and y< len(grid[0]) and grid[x][y]==0