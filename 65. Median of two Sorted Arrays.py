# 二分答案
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        total = len(A)+len(B)
        if total % 2 == 1:
            return self.find_kth(A,B,total // 2+1)
        else:
            left = self.find_kth(A,B,total // 2)
            right = self.find_kth(A,B,total // 2+ 1)
            return (left+right) / 2
        
    def find_kth(self,A,B,k):
        if len(A) == 0:
            left, right = B[0],B[-1]
        elif len(B) == 0:
            left,right = A[0],A[-1]
        else:
            left,right = min(A[0],B[0]),max(A[-1],B[-1])
            
        while left + 1 < right:
            mid = (left + right) // 2
            
            # see how many elements in A less equal than mid 
            count1 = self.helper(A,mid)
            count2 = self.helper(B,mid)
            if count1+count2<k:
                left = mid 
            else:
                right = mid 
        
        count1 = self.helper(A,left)
        count2 = self.helper(B,left)
        
        if count1 + count2 >= k:
            return left
        else:
            return right 
    
    def helper(self,array,target):
        if len(array) == 0:
            return 0
        left, right = 0,len(array) -1 
        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] <= target:
                left = mid 
            else:
                right = mid 
        if array[right] <= target:
            return right + 1 
        if array[left] <= target:
            return left + 1
        return 0
            
        