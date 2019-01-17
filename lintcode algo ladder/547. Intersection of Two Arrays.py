# coding:utf-8
# solution 1: use hashset
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    # def intersection(self, nums1, nums2):
    #     # write your code here
    #     set1 = set(nums1)
    #     set2 = set(nums2)
    #     return list(set1.intersection(set2)) 

# solution 2: binary search & hashset
    
    def intersection(self,nums1,nums2):
        result = set()
        if len(nums1) > len(nums2):
            s_nums = nums2
            b_nums = nums1 
        else:
            s_nums = nums1
            b_nums = nums2
        
        s_nums.sort()
        for num in b_nums:
            if self.binary_search(s_nums,num):
                result.add(num)
        return result
    
    def binary_search(self,nums.target):
        if not nums or len(nums) == 0:
            return False
        
        start,end = 0, len(nums) -1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid 
            else:
                end = mid
            
        if nums[end] == target or nums[start] == target:
            return True
        return False 
# Solution 3: two pointers
    def intersection(self, nums1, nums2):
            # idea: two pointers 
            nums1.sort()
            nums2.sort()
            result = []
    
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] == nums2[j]:
                    result.append(nums1[i])
                    i += 1
                    j += 1
                    while i < len(nums1) and nums1[i] == nums1[i - 1]:
                        i += 1
                    while j < len(nums2) and nums2[j] == nums2[j - 1]:
                        j += 1
                        
                elif nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
    
            return result
    
            
        
        