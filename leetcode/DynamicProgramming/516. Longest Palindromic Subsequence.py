class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # this is a dp problem
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        
        for i in range(len(s)):
            dp[i][i] = 1
            
        result = 1
        for i in range(len(s)-1,-1,-1):
            # print(i)
            for j in range(i,len(s)):
                # print(j)
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    result = max(dp[i][j],result)
        
        return result