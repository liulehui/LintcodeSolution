
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        
        if len(nums) == 0:
            return [[]]
        
        nums.sort()
        subset = []
        self.helper(nums,0,subset,results)
        return results
    
    def helper(self,nums,start_index,subset,results):
        subset_clone = subset[:] # need deep copy here
        results.append(subset_clone)
        for i in range(start_index,len(nums)):
            subset.append(nums[i])
            self.helper(nums,i+1,subset,results)
            subset.pop()