class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return len(s) == 0
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True 
        
        max_length = max([len(x) for x in dict])
        for i in range(1,n+1):
            for j in range(1,min(max_length,i)+1):
                if dp[i-j] == False:
                    continue
                if s[i-j:i] in dict:
                    dp[i] = True
                    break 
        
        return dp[n]
            