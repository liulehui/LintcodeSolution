KEYBOARD = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        if not digits and len(digits) == 0:
            return []
            
        results = []
        subset = ''
        self.helper(digits,0,subset,results)
        return results
    
    def helper(self,digits,index,subset,results):
        if len(subset) == len(digits):
            subset_copy = subset[:]
            results.append(subset_copy)
            return 
        
        for i in KEYBOARD[digits[index]]:
            subset = subset+i
            self.helper(digits,index+1,subset,results)
            subset = subset[0:len(subset)-1]
        
        
