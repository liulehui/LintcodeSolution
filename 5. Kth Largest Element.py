# coding:utf-8

def kthLargestElement(n, nums):
        # write your code here
        if not nums or len(nums) < n or n < 1:
            return None
        
        return quickselect(nums,n,0,len(nums)-1)
        
    
def quickselect(A,k,start,end):
    if start >= end:
        return A[start]
        
    pivot = A[start+(end-start)//2]
    left,right = start,end
    while left <= right:
        while left <= right and A[left] > pivot:
            left += 1 
        while left <= right and A[right] < pivot:
            right -= 1
        
        if left <= right:
            A[left], A[right] = A[right], A[left]
            left += 1 
            right -= 1 
    print(A)  
    if start + k - 1 <= right:
        return quickselect(A,k,start,right)
    if start + k - 1 >= left:
        return quickselect(A,k - (left-start),left,end)
        
    return A[k-1]
    
print(kthLargestElement(3,[9,3,2,4,8]))
