class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # first position of x >= target
        # last position of y <= target
        
        result = []
        
        # first positioin of x >= target
        if not nums:
            return [-1,-1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            print(mid)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        if nums[left] == target:
            result.append(left)
        elif nums[right] == target:
            result.append(right)
        else:
            result.append(-1)
        # last position of x <= target
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            result.append(right)
        elif nums[left] == target:
            result.append(left)
        else:
            result.append(-1)
        
        return result