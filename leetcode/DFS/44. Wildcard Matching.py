class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = {}
        # [[False for _ in range(len(s)) for _ in range(len(p))]
        return self.helper(s,0,p,0,dp)
    
    # search if s start from i and p start from j match or not
    def helper(self,s,i,p,j,dp):
        
        if (i,j) in dp:
            return dp[(i,j)]
        # if s has no char after i
        if len(s) == i:
            for index in range(j,len(p)):
                if p[index] != "*":
                    return False
            return True
        
        if len(p) == j:
            return False
        
        if p[j] != "*":
            matched = self.isMatchChar(p[j],s[i]) and self.helper(s,i+1,p,j+1,dp)
        else:
            matched =  self.helper(s,i+1,p,j,dp) or self.helper(s,i,p,j+1,dp)
        
        dp[(i,j)] = matched
        return matched
    def isMatchChar(self,char1,char2):
        return char1 == char2 or char1 == "?"