class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits or len(digits) == 0:
            return []
        result = []
        digits = digits[::-1]
        c = 1
        for i in range(len(digits)):
            res = (c + digits[i]) % 10
            c = (c + digits[i]) // 10
            result.append(res)
            print(res)
        
        if c != 0:
            result.append(c)
        
        return result[::-1]