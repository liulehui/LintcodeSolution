# coding:utf-8
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        
        if not prerequisites or numCourses < 1 or len(prerequisites) < 1:
            return True
        
        in_degree = [0] * numCourses
        
        edges = {}
        for i in range(numCourses):
            edges[i] = []
        
        for pair in prerequisites:
            if pair[0] in edges[pair[1]]:
                continue
            edges[pair[1]].append(pair[0])
            in_degree[pair[0]] += 1
        
        queue = deque([])
        res = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                # res.append(i)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for neighbor in edges[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(res) == numCourses