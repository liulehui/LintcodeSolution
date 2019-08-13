class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # similar to combination sum if you want all the specific result
        # but here we only need the number of result
        results = 0
        
        dp = [0 for _ in range(amount+1)]
        # here to avoid redundancy, first row is to calculate the result
        # only use coin == 1
        # then add result by allowing using coin == 2
        # then coin == 5
        dp[0] = 1
        
        for coin in coins:
            for i in range(1, amount+1):
                if i >= coin:
                    dp[i] += dp[i - coin]
                # print(dp[i])
        
        return dp[amount]
            
        
        
        