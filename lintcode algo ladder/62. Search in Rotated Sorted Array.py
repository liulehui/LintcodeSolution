# coding:utf-8
def search(A, target):
        # write your code here
        if A is None or len(A) == 0:
            return -1
        def FindMin(A):
            
            start = 0
            end = len(A) - 1 
            target = A[end]
            while start + 1 < end:
                mid = start + (end - start) // 2
                if A[mid] > target:
                    start = mid
                else:
                    end = mid 
            if A[start] <= A[end]:
                return start
            else:
                return end
        def isFind(A,start,end,target):
            while start + 1 < end:
                mid = ( start + end ) // 2
            
                if A[mid] > target:
                    end = mid
                else:
                    start = mid
                
            if A[start] == target:
                return start
            if A[end] == target:
                return end
            return -1
            
            
        min_index = FindMin(A)
        
        index_1 = isFind(A,0,min_index-1,target)
        index_2 = isFind(A,min_index,len(A)-1,target)
        
        if index_1 != -1:
            return index_1
        if index_2 != -1:
            return index_2
        return -1

if __name__  == '__main__':
    