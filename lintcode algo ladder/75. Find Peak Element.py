#coding:utf-8
def findPeak(A):
        # write your code here
        start = 0
        end = len(A) - 1 
        def isPeak(index,A):
            if A[index] > A[index-1] and A[index] > A[index+1]:
                return True
            else:
                return False
                
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if A[mid] > A[mid - 1]:
                if A[mid] > A[mid + 1]:
                    return mid
                else:
                    start = mid
            if A[mid] <= A[mid - 1]:
                end = mid
        
        if isPeak(start,A):
            return start
        if isPeak(end,A):
            return end 
        return -1

A = [1, 2, 1, 3, 4, 5, 7, 6]
print(findPeak(A))