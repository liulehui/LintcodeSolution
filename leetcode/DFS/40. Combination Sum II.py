class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates.sort()
        
        self.helper(candidates,0,[],target,results)
        
        return results
    def helper(self,nums,start_index,result,target,results):
        # exit of recursion
        if start_index >= len(nums) or target <= 0:
            if target == 0:
                results.append(list(result))
            return 
        
        for i in range(start_index,len(nums)):
            # take a look at here more
            if i > start_index and nums[i] == nums[i-1]:
                continue
            result.append(nums[i])
            self.helper(nums,i+1,result,target - nums[i],results)
            result.pop()
        
        