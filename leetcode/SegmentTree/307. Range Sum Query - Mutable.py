# solution 1 segment tree
class SegmentTree(object):

    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None 

    @classmethod
    def build(cls, start, end, a):
        if start > end:
            return None
    	
        if start == end:
            return SegmentTree(start, end, a[start])

        node = SegmentTree(start, end, a[start])

        mid = (start + end) / 2
        node.left = cls.build(start, mid, a)
        node.right = cls.build(mid + 1, end, a)
        node.sum = node.left.sum + node.right.sum
        return node

    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return

        if root.start == root.end:
            root.sum = value
            return
    
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        
        root.sum = root.left.sum + root.right.sum

    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:
            return root.sum
        
        return cls.query(root.left, start, end) +  \
               cls.query(root.right, start, end)
    
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = SegmentTree.build(0, len(nums)-1, nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        SegmentTree.modify(self.root, i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return SegmentTree.query(self.root, i, j)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)