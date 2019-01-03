# coding:utf-8
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if not prerequisites or numCourses<=1 or len(prerequisites) <= 1:
            return True 
        
        in_degree = [0] * numCourses 
        #edges = {i:() for i in range(numCourses)  }
        edges = {}
        for i in range(numCourses):
            edges[i] = []
        
        
        for pair in prerequisites:
            if pair[0] in edges[pair[1]]:
                continue
            edges[pair[1]].append(pair[0])
            in_degree[pair[0]] += 1
        
        
        queue = collections.deque([])
        result = []
        #count = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                #result.append(i)
        #print(queue)
        
        
        while queue:    
            course = queue.popleft()
            result.append(course)
            #count += 1
            for x in edges[course]:
                in_degree[x] -= 1 
                if in_degree[x] == 0:
                    queue.append(x)
        return len(result) == numCourses
                    
            
            
            
            
