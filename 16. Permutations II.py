# coding:utf-8
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return nums
        
        nums.sort()
        
        results = []
        permutation = []
        visited = [False] * len(nums)
        
        self.helper(nums,visited,permutation,results)
        
        return results
    # definition of recursion
    def helper(self,nums,visited,permutation,results):
        # exit of the recursion
        if len(nums) == len(permutation):
            permutation_copy = permutation[:]
            results.append(permutation_copy)
            return
        for i in range(0,len(nums)):
            if visited[i] == True:
                continue
            if i>0 and nums[i] == nums[i-1] and visited[i-1] == False:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.helper(nums,visited,permutation,results)
            permutation.pop()
            visited[i] = False
        
        
        