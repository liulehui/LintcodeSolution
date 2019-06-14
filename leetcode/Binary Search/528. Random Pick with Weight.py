class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.tot = 0
        self.psum = []
        for i in w:
            self.tot += i
            self.psum.append(self.tot)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        import random
        r = random.randint(0,self.tot-1)
        # print(r)
        left, right = 0, len(self.psum) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if r >= self.psum[mid]:
                left  = mid
            else:
                right = mid
        if r < self.psum[left]:
            return left
        else:
            return right
        
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()