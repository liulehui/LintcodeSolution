class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums is None:
            return []
        
        if len(nums) == 0:
            return [[]]
        
        results = []
        nums.sort()
        subset = []
        self.helper(nums,0,subset,results)
        return results 
    
    def helper(self,nums,startIndex,subset,results):
        subset_copy = subset[:]
        results.append(subset_copy)
        
        for i in range(startIndex,len(nums)):
            if nums[i] == nums[i-1] and i>startIndex:
                continue
            subset.append(nums[i])
            self.helper(nums,i+1,subset,results)
            subset.pop()
        
        