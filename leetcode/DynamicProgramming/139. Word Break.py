class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # solution 1: dp
        n = len(s)
        dp = [False] * (n + 1)
        if len(wordDict) == 0:
            return False
        dp[0] = True
        wordSet = set(wordDict)
        max_len = max([len(w) for w in wordDict])
        
        for i in range(1, n+1):
            for j in range(1, min(i, max_len) + 1):
                if not dp[i - j]:
                    continue
                if s[i-j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]
        