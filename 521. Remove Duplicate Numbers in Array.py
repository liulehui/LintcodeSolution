# coding: utf-8

# O(n) time and O(n) space
def deduplication(nums):
        # write your code here
        slow, fast = 0,0
        d = {}
        while fast < len(nums):
            if nums[fast] not in d:
                d[nums[fast]] = True
                nums[slow] = nums[fast]
                slow += 1 
            fast += 1 
        return slow

