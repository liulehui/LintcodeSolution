class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        if n == 0:
            return []
        target = n
        
        self.helper(1, k, [], results, n)
        return results
        
    def helper(self, start_index, k, result, results, target):
        # exit of the recursion
        if len(result) == k and target == 0:
            results.append(list(result))
            return
        
        if len(result) > k or target < 0:
            return
        
        for i in range(start_index, 10):
            result.append(i)
            self.helper(i+1, k, result, results, target - i)
            result.pop()