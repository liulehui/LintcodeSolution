class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_a = len(nums1)
        len_b = len(nums2)
        if not nums1:
            len_a = 0
        
        if not nums2:
            len_b = 0
        
        # 二分答案
        total = len_a + len_b
        
        if total % 2 == 1:
            return self.findkth(nums1,nums2,total // 2 + 1)
        else:
            result = self.findkth(nums1,nums2,total // 2) + self.findkth(nums1,nums2,total // 2 + 1)
            return result / 2.0
        
    def findkth(self,A,B,target):
        if not A or len(A) == 0:
            left, right = B[0], B[-1]
        
        elif not B or len(B) == 0:
            left, right = A[0], A[-1]
        else:
            left, right = min(A[0],B[0]), max(B[-1], A[-1])
        
        
        
        while left + 1 < right:
            mid = (left + right) // 2

            # see how many elements in A less equal than mid 
            count1 = self.helper(A,mid)
            count2 = self.helper(B,mid)
            if count1 + count2 < target:
                left = mid 
            else:
                right = mid 
        
        count1 = self.helper(A,left)
        count2 = self.helper(B,left)

        print(count1,count2)
        print("left",left)
        print("right",right)
        if count1 + count2 >= target:
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