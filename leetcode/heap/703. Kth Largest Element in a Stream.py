class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq
        self.k = k
        self.heap = []
        for n in nums:
            self.add(n)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# self.k = k
#         self.nums = sorted(nums, reverse= True)
#         self.nums = self.nums[0:k]
#         heapq.heapify(self.nums)
#         if len(self.nums) >= self.k:
#             self.last = heapq.heappop(self.nums)
#         else:
#             self.last = float('-inf')
        

#     def add(self, val: int) -> int:
#         if val <= self.last:
#              return self.last
#         self.last=heapq.heappushpop(self.nums, val)
#         return self.last