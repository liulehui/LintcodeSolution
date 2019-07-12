class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 3:
            return True
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                break
            l += 1
            r -= 1 
        
        if l >= r:
            return True
        return self.isLeftValid(s,l+1,r) or self.isLeftValid(s,l,r-1)
    
    def isLeftValid(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
                