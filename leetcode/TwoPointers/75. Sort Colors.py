# class Solution(object):
#     def sortColors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         index = self.sort(A, 0, 0)
#         self.sort(A, 1, index)
        
#     def sort(self, A, flag, index):
#         start, end = index, len(A) - 1
#         while start <= end:
#             while start <= end and A[start] == flag:
#                 start += 1
#             while start <= end and A[end] != flag:
#                 end -= 1
#             if start <= end:
#                 A[start], A[end] = A[end], A[start]
#                 start += 1
#                 end -= 1
#         return start
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1

        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1
            elif A[index] == 1:
                index += 1
            else:
                A[right], A[index] = A[index], A[right]
                right -= 1