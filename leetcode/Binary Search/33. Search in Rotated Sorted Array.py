class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                # mid falls into first part the array
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                # mid falls into second part of the array
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1