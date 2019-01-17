"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        i = 0 
        j = 0
        
        self.results = []
        
        while i<len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_interval(list1[i])
                i += 1 
            else:
                self.push_interval(list2[j])
                j += 1 
        
        while i < len(list1):
            self.push_interval(list1[i])
            i += 1 
        while j< len(list2):
            self.push_interval(list2[j])
            j += 1 
        
        return self.results
    #  The purpose of this function is to identify whether 
    #  the interval can be merged with the last one already in the results
    def push_interval(self,interval):
        if len(self.results) == 0:
            self.results.append(interval)
            return 
        
        last_interval = self.results[-1]
        if last_interval.end < interval.start:
            self.results.append(interval)
            return 
        
        self.results[-1].end = max(self.results[-1].end,interval.end)
            