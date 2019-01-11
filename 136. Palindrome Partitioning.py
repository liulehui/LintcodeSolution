class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return []
        results = []
        self.dfs(s,[],results)
        return results
    
    def dfs(self,s,subset,results):
        if len(s) == 0:
            
            results.append(subset)
            return 
        
        for i in range(1,len(s)+1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                self.dfs(s[i:],subset+[prefix],results)
            
    def is_palindrome(self,s):
        return s == s[::-1]
            
                
        
        
