# coding:utf-8
class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return nums
        
        if len(nums) == 1:
            return nums
        
        i = len(nums) - 1 
        while i>0 and nums[i] <= nums[i-1]:
            i -= 1
        
        print(i)
        
        if i != 0:
            j = len(nums) - 1 
            while nums[j] <= nums[i - 1]:
                j -= 1 
            self.swap_item(nums,i-1,j)
        
        self.swap_list(nums,i,len(nums)-1)
        return nums 
    
    def swap_item(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i] 
    
    def swap_list(self,nums,i,j):
        while i<j:
            self.swap_item(nums,i,j)
            i += 1 
            j -= 1 
