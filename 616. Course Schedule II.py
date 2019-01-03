#coding:utf-8
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if numCourses == 0:
            return []
        if numCourses == 1:
            return [0]
        
        indegree = [0] * numCourses
        edges = {i:[] for i in range(numCourses)}
        
        result = []
        queue = collections.deque()
        
        for pair in prerequisites:
            edges[pair[1]].append(pair[0])
            indegree[pair[0]] += 1 
        
        for i in range(numCourses):
            if indegree[i] == 0:
                #result.append(i)
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for x in edges[node]:
                indegree[x] -= 1 
                if indegree[x] == 0:
                    queue.append(x)
                    #result.append(x)
        print(result)
        if len(result) == numCourses:
            return result
        else:
            return []
            
            