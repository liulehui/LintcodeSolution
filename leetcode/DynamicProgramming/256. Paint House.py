# coding:utf-8
class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        
        dp = [[0 for _ in range(3)] for _ in range(len(costs))]
        
        dp[0] = costs[0]
        
        for i in range(1,len(costs)):
            print(dp[i-1])
            print("i = ", i)
            dp[i][0] = costs[i][0] + min(dp[i-1][1],dp[i-1][2])
            print(dp[i][0])
            print(dp[i-1])
            dp[i][1] = costs[i][1] + min(dp[i-1][0],dp[i-1][2])
            print(dp[i][1])
            print(dp[i-1])
            dp[i][2] = costs[i][2] + min(dp[i-1][1],dp[i-1][0])
            print(dp[i][2])
            print(dp[i-1])
                
        return min(dp[-1])
        
        