class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return 0
        nums = sorted(nums)[::-1]
        res = 0
        for i in range(0,len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    left += 1
                else:
                    right -= 1
                
        return res
                
        