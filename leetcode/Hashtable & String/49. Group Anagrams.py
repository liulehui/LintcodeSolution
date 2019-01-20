class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for str in strs:
            str_sorted = ''.join(sorted(str)) # klogk
            if str_sorted not in dict:
                dict[str_sorted] = [str]
            else:
                dict[str_sorted].append(str)
        
        res = []
        for key in dict:
            res.append(dict[key])
        
        return res
        
        