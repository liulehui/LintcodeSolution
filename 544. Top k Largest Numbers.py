# coding:utf-8
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        import heapq
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap,(num))
            
            if len(self.heap) > k:
                heapq.heappop(self.heap) 
            
        
        res = []
        while len(self.heap) != 0:
            num = heapq.heappop(self.heap)
            res.append(num) 
        res.reverse()
        return res 
            
