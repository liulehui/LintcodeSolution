class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        self.dfs(s, 0, [], {}, results)
        return results
        
    def generate_solution(self, s, partition):
        strings = []
        last_index = -1
        for i in partition:
            strings.append(s[last_index + 1: i + 1])
            last_index = i
        return strings
        
    def get_is_palindrome(self, memo, s, i, j):
        if (i, j) in memo:
            return memo[(i, j)]
            
        if i == j:
            return True
        if i + 1 == j:
            return s[i] == s[j]
        
        memo[(i, j)] = s[i] == s[j] and self.get_is_palindrome(memo, s, i + 1, j - 1)
        return memo[(i, j)]
        
    def dfs(self, s, index, partition, memo, results):
        if index == len(s):
            results.append(self.generate_solution(s, partition))
            return
            
        for i in range(index, len(s)):
            if not self.get_is_palindrome(memo, s, index, i):
                continue
            partition.append(i)
            self.dfs(s, i + 1, partition, memo, results)
            partition.pop()