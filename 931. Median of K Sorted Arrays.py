# coding:utf-8
# binary search results
# k 个数组，每个数组的平均长度为n

# 时间复杂度为O（log(range)*klogn）
# 因为log(range) 最大为32所以是klogn
# 空间复杂度O（1）

import math 
class Solution:
    """
    @param nums: the given k sorted arrays
    @return: the median of the given k sorted arrays
    """
    def findMedian(self, nums):
        # write your code here
        if nums == None:
            return 0.0
            
        size = self.get_total_size(nums)
        if size == 0:
            return 0.0
        
        smallest, largest = math.inf,-math.inf
        for array in nums:
            if not array:
                continue
            smallest = min(smallest,array[0])
            largest = max(largest,array[-1])
    
    # odd size ==> get the median directly
        if size % 2 == 1:
            return float(self.get_kth_number(nums, size // 2 + 1, smallest, largest))
            
        left = self.get_kth_number(nums, size // 2 , smallest, largest)
        right = self.get_kth_number(nums, size // 2 + 1, left, largest)
        return (left + right) / 2
    
    def get_kth_number(self,nums,k,start,end):
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.number_of_numbers_less_than_or_equal_to(nums,mid) >= k:
                end = mid 
            else:
                start = mid 
        if self.number_of_numbers_less_than_or_equal_to(nums,start) >= k:
            return start 
        
        return end 
    
    def get_number_of_smaller_or_equal(self, array, number):
        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if array[mid] <= number:
                start = mid
            else:
                end = mid
        
        if array[end] <= number:
            return end + 1 
        if array[start] <= number:
            return start + 1 
        return 0
    
    def number_of_numbers_less_than_or_equal_to(self, nums, number):        
        number_of_smaller_or_equal = 0
        for array in nums:
            if not array:
                continue
            if array[0] > number:
                continue
            number_of_smaller_or_equal += self.get_number_of_smaller_or_equal(array, number)
        return number_of_smaller_or_equal
    
    def get_total_size(self, nums):
        size = 0
        for array in nums:
            size += len(array)
        return size
        
        
        
        
        