class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 1.  k size min heap time:O(Nlogk) space: O(k)
        # 2. quick select O(N) O(1)
        
        if not nums or len(nums) < k:
            return None
        
        return self.quickselect(nums,k,0,len(nums)-1)
        # return nums[n-1]
    
    def quickselect(self,A,k,start,end):
        if start == end:
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
        #print(A)  
        if start + k - 1 <= right:
            return self.quickselect(A,k,start,right)
        if start + k - 1 >= left:
            return self.quickselect(A,k - (left-start),left,end)
            
        return A[start + k-1]
        