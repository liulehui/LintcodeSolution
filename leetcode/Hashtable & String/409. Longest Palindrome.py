class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # time O(n)
        
        dict = {}
        if not s or len(s) == 0:
            return 0
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        length = 0
        for key in dict:
            length += dict[key] // 2 * 2
            if length % 2 == 0 and dict[key] % 2 == 1:
                length += 1
        return length
            
        