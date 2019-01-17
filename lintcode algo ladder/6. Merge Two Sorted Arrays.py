class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        results = []
        if A is None or len(A) == 0:
            return B 
        if B is None or len(B) == 0:
            return A 
        
        len_A = len(A)
        len_B = len(B)
        i = 0
        j = 0
        
        while i<len_A and j<len_B:
            if A[i] <= B[j]:
                results.append(A[i])
                i += 1 
            else:
                results.append(B[j])
                j += 1 
        
        if i == len(A):
            while j < len_B:
                results.append(B[j])
                j += 1 
            
        if j == len(B):
            while i < len_A:
                results.append(A[i])
                i += 1 
        
        return results
            
