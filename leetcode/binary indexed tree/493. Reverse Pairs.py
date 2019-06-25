import bisect
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negNums = map(lambda x:-x,nums)
        pairs = 0
        sortedNums = sorted(negNums)
        N = len(negNums)
        BITree = [0] * (N+1)
        
        def count(BITree, before):
            """
            return Indentifier(sortedNums)[0] + Indentifier(sortedNums)[1] +...+ Indentifier(sortedNums)[before]
            """
            start = before + 1
            psum = 0
            while start > 0:
                psum += BITree[start]
                start = start - (start&(-start))
            return psum
        def add(BITree, rank):
            """
            add 1 to Indentifier(sortedNums)[rank]
            """
            start = rank + 1
            while start <= N:
                BITree[start] += 1
                start = start + (start&(-start))
                
            
        for k in negNums:
            before = bisect.bisect_left(sortedNums, k * 2) - 1
            pairs += count(BITree, before)

            rank = bisect.bisect_left(sortedNums,k)
            add(BITree,rank) 

            
        return pairs