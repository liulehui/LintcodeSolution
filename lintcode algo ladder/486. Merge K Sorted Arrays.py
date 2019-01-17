# coding：utf-8 
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        # divide and conquer
        if arrays is None or len(arrays) == 0:
            return []
        if len(arrays) == 1:
            return arrays[0]
        mid = len(arrays) // 2 
        left = self.mergekSortedArrays(arrays[0:mid])
        right = self.mergekSortedArrays(arrays[mid:])
        return self.merge_2_sortedarrays(left,right)
   
    
    def merge_2_sortedarrays(self,A,B):
        if len(A) == 0 or len(B) == 0:
            if len(A) == 0:
                return B 
            if len(B) == 0:
                return A
        
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1  
            else:
                result.append(B[j])
                j += 1 
        
        while i < len(A):
            result.append(A[i])
            i += 1 
        while j < len(B):
            result.append(B[j])
            j += 1 
        
        return result