# coding:utf-8
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    
        
    def heapify(self, A):
        # write your code here
        for i in range(len(A)):
            self.siftup(A,i)

    def siftup(self,A,k):
        while k!=0:
            father = int((k-1)/2)
            if A[k] > A[father]:
                break
            A[father],A[k] = A[k],A[father]
            k = father  
    