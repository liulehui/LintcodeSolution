# coding:utf-8
def twoSum(self, nums, target):
        # write your code here
        left,right = 0,len(nums) - 1 
        
        while left<right:
            if nums[left] + nums[right] < target:
                left += 1 
            if nums[left] + nums[right] > target:
                right -= 1 
            
            if nums[left] + nums[right] == target:
                return left+1,right+1 
        
        return -1