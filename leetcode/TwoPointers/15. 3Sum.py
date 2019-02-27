class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []
        nums.sort()
        results = set()
        for i in range(len(nums)):
            l,r = i+1, len(nums) - 1
            while l < r:
                if l == i:
                    l += 1
                if r == i:
                    r -= 1
                
                if nums[l] + nums[r] == (0 - nums[i]):
                    result = tuple(sorted([nums[l],nums[r],nums[i]]))
                    
                    results.add(result)
                    l += 1
                    r -= 1
                    
                elif nums[l] + nums[r] < (0 - nums[i]):
                    l += 1
                else:
                    r -= 1
        results = list(results)          
        return results