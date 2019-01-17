class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if n == 1:
            return 1 
        
        import heapq
        heap = []
        heapq.heappush(heap,1)
        visited = set()
        visited.add(1)
        for i in range(n):
            val = heapq.heappop(heap)
            for multi in [2,3,5]:
                if val * multi not in visited:
                    visited.add(val*multi)
                    heapq.heappush(heap,val* multi)
        
        return val 
            
