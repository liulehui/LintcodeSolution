class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_dict = {}
        res = 0
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        for k in freq_dict.keys():
            if k + 1 not in freq_dict:
                continue
            res = max(res, freq_dict[k] + freq_dict[k+1])
            
        return res
                
        