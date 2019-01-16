"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        print(len(points))
        for point in points:
            dist = self.get_distance(point,origin)
            
            heapq.heappush(self.heap,(-dist,-point.x,-point.y))
            
            if len(self.heap) > k:
                heapq.heappop(self.heap)
            # print(len(self.heap))
            
        ret = []
        
        while len(self.heap) > 0:
            _,x,y = heapq.heappop(self.heap)
            ret.append(Point(-x,-y))
        ret.reverse()
        return ret 
    def get_distance(self,a,b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
