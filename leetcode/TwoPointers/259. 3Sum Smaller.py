class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(0,len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp_sum = nums[left] + nums[right] + nums[i]
                if tmp_sum < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        return result
            