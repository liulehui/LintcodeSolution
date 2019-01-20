class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        dict1 = [0] * 26
        dict2 = [0] * 26
        for letter in p:
            dict1[ord(letter) - ord('a')] += 1
        
        left, right = 0, len(p) - 1
        res = []
        while right < len(s):
            if left == 0:
                left += 1
                right += 1
                for i in range(len(p)):
                    dict2[ord(s[i])-ord('a')] += 1
                    
                    if self.check2dict(dict1,dict2):
                        res.append(0)
                continue
            
            dict2[ord(s[left -1])-ord('a')] -= 1
            dict2[ord(s[right])-ord('a')] += 1
            
            if self.check2dict(dict1,dict2):
                res.append(left)
            left += 1
            right += 1
        return res
    
    def check2dict(self,dict1,dict2):
        for i in range(26):
            if dict1[i] != dict2[i]:
                return False
        
        return True
                
            
            
            
        