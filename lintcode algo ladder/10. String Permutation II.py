class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    # same as permutation problem
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]
        if len(str) == 0:
            return [""]
        str1 = ''.join(sorted(str))
        results = []
        string = ''
        visited = [False] * len(str)
        self.helper(str1,visited,string,results)
        return results
    
    def helper(self,str,visited,string,results):
        if len(str) == len(string):
            string_copy = string[:]
            results.append(string_copy)
            return 
        
        for i in range(0,len(str)):
            if visited[i]:
                continue
            if i > 0 and str[i] == str[i-1] and visited[i-1] == False:
                continue
            string = string + str[i]
            visited[i] = True
            self.helper(str,visited,string,results)
            visited[i] = False
            string = string[:-1]
            
