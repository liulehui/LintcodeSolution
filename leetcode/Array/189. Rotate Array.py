class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return nums
        
        
        k = k % len(nums)
        
        def reverse(arr, i, j):
            # i, j = 0, len(arr) - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
            
                i += 1
                j -= 1
            
            return arr
        
        n = len(nums)
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
        
        return nums