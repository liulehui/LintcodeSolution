class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        if not nums:
            return self.results
        
        if len(nums) == 0:
            self.results.append([])
            return self.results
        
        nums.sort()
        subset = []
        self.helper(nums,0,subset,self.results)
        
        return self.results
    
    def helper(self,nums,start_index,subset,results):
        results.append(list(subset))
        
        for i in range(start_index, len(nums)):
            subset.append(nums[i])
            self.helper(nums,i+1,subset,results)
            subset.pop()
            
        
        