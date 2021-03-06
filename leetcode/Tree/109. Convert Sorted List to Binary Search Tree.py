# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next
        
        return self.sortedArrayToBST(self.nums)
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.nums = nums
        if not nums:
            return None
        l, r = 0, len(nums) - 1
        return self.helper(l,r)
    
    def helper(self,left,right):
        if left > right:
            return None 
        
        mid = left + (right - left) // 2
        
        node = TreeNode(self.nums[mid])
        if left == right:
            return node
        node.left = self.helper(left,mid - 1)
        node.right = self.helper(mid + 1, right)
        
        return node
        