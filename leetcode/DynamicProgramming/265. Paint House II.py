# coding:utf-8
class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None:
            return 0
        if len(costs) == 0:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        
        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]
        
        dp[0] = costs[0]
        
        for i in range(len(costs)):
            for j in range(len(costs[0])):
                last_row = dp[i-1].copy()
                last_row.pop(j)
                dp[i][j] = costs[i][j] + min(last_row)
        
        return min(dp[-1])
        