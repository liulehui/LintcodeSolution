class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        if not nums:
            return subsets
        
        if len(nums) == 0:
            return subsets.append([])
        
        nums.sort()
        subset = []
        self.helper(nums,0,subset,subsets)
        return subsets
    
    def helper(self,nums,start_index,subset,subsets):
        subsets.append(list(subset))
        
        for i in range(start_index,len(nums)):
            if i != start_index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.helper(nums,i+1,subset,subsets)
            subset.pop()
            
            
        