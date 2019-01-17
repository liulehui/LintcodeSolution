# coding:utf-8
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Solution 1 min heap
from heapq import heappush,heappop
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        # divide and conquer 
        if intervals is None or len(intervals) == 0:
            return [[]]
        
        self.heap = []
        for i,interval in enumerate(intervals):
            if len(interval)>0:
                heappush(self.heap,(interval[0].start,interval[0].end,i,0)) 
        
        ans = []
        #start,end,x,y = heappop(self.heap)
        #print(start,end,x,y)
        
        while len(self.heap) > 0:
            start,end,x,y = heappop(self.heap)
            
            if len(ans) == 0 or ans[-1].end < start:
                ans.append(Interval(start,end))
                
            else:
                ans[-1].end = max(ans[-1].end,end)
            if y+1 < len(intervals[x]):
                heappush(self.heap,(intervals[x][y+1].start,intervals[x][y+1].end,x,y+1))
        
        
        return ans
        
        
        