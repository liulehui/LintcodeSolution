# coding:utf-8
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        # difference from subsets
        # have a target to restrict
        # need to deduplication
        # same repeated number may be chosen from unlimited number of times
        
        # deduplication
        candidates = sorted(list(set(candidates)))
        results = []
        subset = []
        self.dfs(candidates,target,0,subset,results)
        
        return results
    
    def dfs(self,candidates,target,start_index,subset,results):
        if target == 0:
            subset_copy = subset[:]
            results.append(subset_copy)
            return
        for i in range(start_index,len(candidates)):
            if target < candidates[i]:
                return
            
            subset.append(candidates[i])
            self.dfs(candidates,target-candidates[i],i,subset,results)
            subset.pop()
        
        
        
