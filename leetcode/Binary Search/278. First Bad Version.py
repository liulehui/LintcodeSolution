# coding:utf-8
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if isBadVersion(mid) == True:
                end  = mid
            else:
                start = mid
            
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end
        
        return 0
        