class Solution(object):
    class BIT:
        def __init__(self, n):
            self.n = n + 1
            self.sums = [0] * self.n

        def update(self, i, delta):
            while i < self.n:
                self.sums[i] += delta
                i += i & (-i)

        def query(self, i):
            res = 0
            while i > 0:
                res += self.sums[i]
                i -= i & (-i)
            return res

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BIT O(nlogn)
        new_nums = nums + [x * 2 for x in nums] 
        # 这一步非常机智，这样就扯平了importanct reverse的不同
        # 不需要bisect了
        
        sorted_set = sorted(list(set(new_nums)))
        tree = self.BIT(len(sorted_set))
        res = 0
        ranks = {}
        for i, n in enumerate(sorted_set):
            ranks[n] = i + 1
        # The question requires nums[i] > 2*nums[j], 
        # so the question can be transferred to, for each nums[i], how many num * 2 at its right (nums[j]) is smaller than it. 
        # Now we can find the problem is similar to LC 315 (Count of smaller numbers after self).
        # The rank is used to map the number to the sorted list idx and BIT idx.
        # BIT is used to store the frequency of nums at each rank. 
        # We iterate original nums from right to left, then update num * 2 on BIT. 
        # So every time we do a query(ranks[n] - 1),
        # then we can get the total frequency of what we want.
        for n in nums[::-1]:
            res += tree.query(ranks[n] - 1)
            tree.update(ranks[n * 2], 1)

        return res