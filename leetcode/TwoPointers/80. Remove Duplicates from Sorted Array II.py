class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)
        
        l, r = 1, 2
        
        while r < len(nums):
            if nums[r] == nums[l] and nums[r] == nums[l - 1]:
                    r += 1
            else:
                nums[l + 1] = nums[r]
                l += 1
                r += 1
        return l + 1
                
                