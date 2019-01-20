# coding:utf-8
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        diction = {} 
        for letter in s:
            if letter not in diction:
                diction[letter] = 1
            else:
                diction[letter] += 1 
        
        for letter in t:
            if letter not in diction or diction[letter] == 0:
                return False
            diction[letter] -= 1 
        
        return True
            