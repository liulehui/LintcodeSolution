# coding:utf-8
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums) == 1:
            return nums
        
        if nums is None:
            return None 
        
        i = len(nums)-1
        while i != 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        
        if i != 0:
            j = len(nums) - 1
            while nums[j] <= nums[i-1]:
                j -= 1 
            self.swap_element(nums,i-1,j)
        print(i)
        self.swap_list(nums,i,len(nums)-1)
        return nums
    def swap_element(self,nums,i,j):
        nums[i],nums[j] = nums[j],nums[i]
    
    def swap_list(self,nums,i,j):
        while i<j:
            self.swap_element(nums,i,j)
            i += 1 
            j -= 1 
        