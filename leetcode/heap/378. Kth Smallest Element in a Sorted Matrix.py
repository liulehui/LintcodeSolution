class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        dirs = [[0, 1], [1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False] * n for _ in range(n)]
        heap = []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        count = 0
        while len(heap) > 0 and count < k:
            result, x, y = heapq.heappop(heap)
            count += 1 
            for dir in dirs:
                next_x = x + dir[0]
                next_y = y + dir[1]
                if next_x < 0 or next_x >= m or next_y < 0 or next_y >= n or visited[next_x][next_y]:
                    continue 
                
                heapq.heappush(heap, (matrix[next_x][next_y], next_x, next_y))
                visited[next_x][next_y] = True
                
        return result
        