class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        target = nums[-1]
        # find the first position <= target
        while l + 1 < r:
            mid = ( l + r ) // 2
            if nums[mid] > target:
                l = mid
            else:
                r = mid
        if nums[l] < target:
            return nums[l]
        else:
            return nums[r]
            
        return 