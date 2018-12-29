# coding:utf-8

def mountainSequence(nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return 0
        
        leng = len(nums)
    
        left = 0
        right = leng - 1 
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                # on the downside of the mountainSequence
                right = mid
            else:
                left = mid
        
        maxi = max(nums[left],nums[right])
        return maxi 

a = [1, 2, 4, 8, 6, 3]
b = [10,9,8,7]

print(mountainSequence(a))
print(mountainSequence(b))