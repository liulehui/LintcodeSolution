class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s or len(s) == 0:
            return True
        
        # s = s.split()
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
        
            l += 1
            r -= 1 
        
        return True
        
        
        