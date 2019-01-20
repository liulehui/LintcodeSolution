# coding:utf-8
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        dict_t = collections.Counter(t)
        print(dict_t)
        
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        
        l, r = 0, 0
        
        formed = 0 # keep track of how many unique characters in t are present in the current window in its desired frequency.
        
        window_counts = {}
        
        ans = float("inf"), None, None # ans tuple of the form (window length, left, right)
        
        while r < len(s):
            # add one char from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1


            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1  
        
        # Keep expanding the window once we are done contracting.
            r += 1   
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]