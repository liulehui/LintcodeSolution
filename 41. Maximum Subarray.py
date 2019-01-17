class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    # prefix sum
    def maxSubArray(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return 0
        
        max_sum = -sys.maxsize
        presum = 0
        min_sum = 0
        for i in range(len(nums)):
            # TODO: write code...
            presum += nums[i]
            max_sum = max(max_sum,presum - min_sum)
            min_sum = min(min_sum,presum)
        
        return max_sum