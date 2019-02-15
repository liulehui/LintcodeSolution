# coding:utf-8
# Solutions:
# to shrink the left and right
# time: O(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            maxArea = max(maxArea,min(height[left],height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
            
