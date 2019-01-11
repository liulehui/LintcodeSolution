class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if s is None:
            return []
        
        if len(s) == 0:
            return [[]]
            
        results = []
        subset = []
        self.helper(s,0,subset,results)
        return results
    
    def helper(self,s,start_index,subset,results):
        if start_index == len(s):
            subset_copy = subset[:]
            results.append(subset_copy)
            return 
        
        for i in range(start_index,len(s)):
            if i >= start_index+2:
                break
            split = s[start_index:i+1]
            subset.append(split)
            self.helper(s,i+1,subset,results)
            subset.pop()
            