# coding:utf-8
def kClosestNumbers(A, target, k):
    # write your code here
    def isLeftCloser(A,left,right):
        if right > len(A) - 1:
            return True
        if left < 0:
            return False
        if abs(A[left]-target) <= abs(A[right]-target):
            return True
        else:
            return False
            
        
    if A is None or len(A) == 0:
        return []
    ans = []
    start = 0
    end = len(A) - 1
    
    while start + 1 < end:
        mid = start + (end - start) // 2
        
        if A[mid] < target:
            start = mid
        else:
            end = mid
    # find the left which start from here
    left = 0
    if A[end] <= target:
        left = end
    else:
        left = start
    right = left + 1
    
    while len(ans) < k:
        if isLeftCloser(A,left,right):
            ans.append(A[left])
            left-=1
        else:
            ans.append(A[right])
            right+=1

    return ans

A = [1,4,6,10,20]
target = 21
k = 4
print(kClosestNumbers(A,target,k))