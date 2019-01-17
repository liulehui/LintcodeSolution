# coding: utf-8
def partitionArray(nums, k):
# write your code here
	left = 0
	right = len(nums) - 1 
	# print(left,right)
	while left<= right:
		while left<=right and nums[left] < k:
			left += 1
			# print(left,right)
		while left <= right and nums[right] >= k:
			right -= 1 
			# print(left,right)
		if left <= right:
			nums[left],nums[right] = nums[right],nums[left]
			left += 1 
			right -= 1  
			# print(left,right)
		# print(left,right)  
	return left

print(partitionArray([3,2,1],2))

