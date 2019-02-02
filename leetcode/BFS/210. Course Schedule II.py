class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        from collections import deque
        
        if numCourses < 1:
            return []
        
        res = []
        if len(prerequisites) < 1:
            
            for i in range(numCourses):
                res.append(i)
            return res
        
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
        # res = []
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
        
        if len(res) == numCourses:
            return res
        else:
            return []