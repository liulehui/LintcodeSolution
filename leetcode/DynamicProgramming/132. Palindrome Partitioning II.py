class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp records from i-th element to the end
        # can be divided into minimal number of pali strings
        dp = [0 for i in range(len(s)+1)]
        isPali = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s)-i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ((j in [i, i+1]) or isPali[i+1][j-1]):
                    isPali[i][j] = True
                    dp[i] = min(dp[i], dp[j+1]+1)
        return dp[0] - 1

        
            
        
                