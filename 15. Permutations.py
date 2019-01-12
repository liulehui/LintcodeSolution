class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums is None:
            return None 
        results = []
        nums.sort()
        permutation = []
        visited = [False] * len(nums)
        self.helper(nums,visited,permutation,results)
        return results
    # definition of the recursion
    def helper(self,nums,visited,permutation,results):
        # exit of the recursion
        if len(nums) == len(permutation):
            permutation_copy = permutation[:]
            results.append(permutation_copy)
            print(permutation_copy)
            return 
        
        # divide of the recursion
        for i in range(0,len(nums)):
            if visited[i]:
                continue
            
            permutation.append(nums[i])
            visited[i] = True
            self.helper(nums,visited,permutation,results)
            visited[i] = False
            permutation.pop()
        