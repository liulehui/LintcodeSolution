class SegmentTree(object):
    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None 
    
    @classmethod
    def build(cls, start, end):
        if start > end:
            return None
    	
        if start == end:
            return SegmentTree(start, end)

        node = SegmentTree(start, end)

        mid = (start + end) / 2
        node.left = cls.build(start, mid)
        node.right = cls.build(mid + 1, end)
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
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        min_val = min(nums)
        max_val = max(nums)
        self.root = SegmentTree.build(min_val,max_val)
        nums = nums[::-1]
        result = []
        for i in range(len(nums)):
            res = SegmentTree.query(self.root,min_val,nums[i]-1)
            origin = SegmentTree.query(self.root,nums[i],nums[i])
            SegmentTree.modify(self.root,nums[i],origin+1)
            result.append(res)
        
        return result[::-1]