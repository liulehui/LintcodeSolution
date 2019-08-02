class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        candidates.sort()
        self.helper(candidates,0,[],target,results)
        
        return results
    
    def helper(self,nums,start_index,combination,target,results):
        if start_index == len(nums) or target <= 0:
            if target == 0:
                results.append(list(combination))
            return
        
        for i in range(start_index,len(nums)):
            combination.append(nums[i])
            self.helper(nums,i,combination,target - nums[i],results)
            combination.pop()
        
        