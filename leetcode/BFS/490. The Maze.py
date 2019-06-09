class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        from collections import deque
        R, C = len(maze), len(maze[0])
        q = deque()
        q.append(start)
        seen = set(start)
        while q:
            for each in range(len(q)):
                x, y = q.popleft()
                for each in [1,0],[0,1],[-1,0],[0,-1]:
                    tempx, tempy, xo, yo = x, y, each[0], each[1]
                    # 这一步while就是找到这个方向的边界了
                    while 0 <= tempx + xo < R and 0 <= tempy + yo < C and maze[tempx+ xo][tempy + yo] != 1: 
                        tempx, tempy = tempx + xo, tempy + yo
                    if (tempx, tempy) not in seen:
                        q.append([tempx, tempy])
                        seen.add((tempx, tempy))
                        if [tempx, tempy] == destination: return True
        return False 
        