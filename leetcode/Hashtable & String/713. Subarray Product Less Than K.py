# coding:utf-8
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        left = 0
        
        product = 1
        res = 0
        
        for right, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[left]
                left += 1
            
            res += right - left + 1
        
        return res
        