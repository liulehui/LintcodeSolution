class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                else:
                    result[i][j] = self.bfs(i,j,matrix)
        return result
    
    def bfs(self,i,j,matrix):
        self.directions = [(0,1),(0,-1),(1,0),(-1,0)]
        from collections import deque
        queue = deque([(i,j)])
        result = 0
        while queue:
            result += 1
            level = []
            for i in range(len(queue)):
                x, y = queue.popleft()
                for delta_x, delta_y in self.directions:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if self.is_valid(new_x,new_y,matrix):
                        if matrix[new_x][new_y] == 0:
                            return result
                        else:
                            queue.append((new_x,new_y))
                    
    def is_valid(self,i,j,matrix):
        return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])     
        