class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if k > n:
            return None 
        
        if n == 0:
            return []
        
        results = []
        self.helper(n,1,[],results,k)
        
        return results
    
    def helper(self,n,start_index,combination,results,k):
        if len(combination) == k:
            combination_copy = combination[:]
            print(combination_copy)
            results.append(combination_copy)
            
            return
        
        for i in range(start_index,n+1):
            combination.append(i)
            self.helper(n,i+1,combination,results,k)
            combination.pop()
        