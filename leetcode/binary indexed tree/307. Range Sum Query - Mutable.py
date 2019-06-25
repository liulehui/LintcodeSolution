class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        # initialization for this one
        # in add, we first self increase 1 on index to even the bit and arr
        for i in range(self.n):
            self.add(i, self.arr[i])
        
    def add(self,index,val):
        index += 1
        while index <= self.n:
            self.bit[index] += val
            index += self.lowbit(index)
    
    def lowbit(self,x):
        return x&(-x)
    
    def sum(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= self.lowbit(idx)
        return res
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.add(i, val - self.arr[i])
        self.arr[i] = val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)