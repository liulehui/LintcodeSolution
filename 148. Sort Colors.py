# coding:utf-8
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        # partition
        index = self.sort(nums,0,0)
        # print(index)
        # print(nums)
        self.sort(nums,1,index)
        print(nums)
        return 
        
    def sort(self,A,flag,index):
        left = index
        right = len(A) - 1 
        while left <= right:
            while left <= right and A[left] == flag:
                left += 1 
            while left <= right and A[right] != flag:
                right -= 1 
            
            if left <= right:
                A[left],A[right] = A[right],A[left]
                left += 1 
                right -= 1 
        
        return left 
        
A = Solution()
A.sortColors([1, 0, 1, 2])
