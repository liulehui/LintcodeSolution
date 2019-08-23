class Solution(object):
    def isMatch(self,s,p):
        s_len = len(s)
        p_len = len(p)
        # edge case
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False
        
        dp = [[False] * (s_len + 1) for _ in range(p_len+1)]
        dp[0][0] = True
        
        # compute DP
        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1
                # d[p_idx - 1][s_idx - 1] is a string-pattern match 
                # on the previous step, i.e. one character before.
                # Find the first idx in string with the previous math.
                while not dp[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                
                # If (string) matches (pattern), 
                # when (string) matches (pattern)* as well
                dp[p_idx][s_idx - 1] = dp[p_idx - 1][s_idx - 1]
                # If (string) matches (pattern), 
                # when (string)(whatever_characters) matches (pattern)* as well
                while s_idx < s_len + 1:
                    dp[p_idx][s_idx] = True
                    s_idx += 1
                
            elif p[p_idx - 1] = '?':
                for s_idx in range(1, s_len + 1): 
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] 
            # the current character in the pattern is not '*' or '?'
            else:
                for s_idx in range(1, s_len + 1): 
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    dp[p_idx][s_idx] = dp[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]  
                                                               
        return dp[p_len][s_len]