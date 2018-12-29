# coding:utf-8
def findMin(nums):
        # write your code here
        start = 0
        end = len(nums) - 1
        
        target = nums[end]
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] < target:
                end = mid
            else:
                start = mid
                
        if nums[start] < target:
            return nums[start]
        else:
            return nums[end]
A = [4, 5, 6, 7, 0, 1, 2]
print(findMin(A))