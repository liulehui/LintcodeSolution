class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.map = {
                        '2': 'abc',
                        '3': 'def',
                        '4': 'ghi',
                        '5': 'jkl',
                        '6': 'mno',
                        '7': 'pqrs',
                        '8': 'tuv',
                        '9': 'wxyz',
                    }
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, '', results)
        
        return results
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return
        
        for letter in self.map[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)