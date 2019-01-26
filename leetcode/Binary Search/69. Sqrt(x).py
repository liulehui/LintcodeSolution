class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # find the last element whose square less or equal than x
        start, end = 1, x
        while start + 1 < end:
            mid  = (start + end) // 2
            if mid ** 2 <= x:
                start = mid
            else:
                end = mid
        
        if end ** 2 <= x:
            return end
        if start ** 2 <= x:
            return start
        
        return -1