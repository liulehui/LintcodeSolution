# coding:utf-8
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
# Solution 1  Priority Queue and Heap
# from heapq import heappop, heappush
# class Solution:
#     """
#     @param lists: a list of ListNode
#     @return: The head of one sorted list.
#     """
#     def mergeKLists(self, lists):
#         # write your code here
#         self.sequence = 0
#         if not lists:
#             return None
        
#         trav = dummy = ListNode(-1)
#         heap = []
#         for list in lists:
#             if list:
#                 self.heappushNode(heap,list)
        
#         while heap:
#             node = heappop(heap)[2]
#             trav.next = node
#             trav = trav.next 
#             if trav.next:
#                 self.heappushNode(heap,trav.next)
        
#         return dummy.next
        
#     def heappushNode(self,heap,node):
#         self.sequence += 1 
#         heappush(heap,(node.val,self.sequence,node))
# Solution 2 Divide and conquer
class Solution:
    def mergeKLists(self,lists):
        # write your code here
        if len(lists) < 1:
            return None
        if len(lists) == 1:
            return lists[0]
            
        
        
        return self.helper(lists,0,len(lists)-1)
    
    def helper(self,lists,start,end):
        if start == end:
            return lists[start]
        
        mid = start + (end - start) // 2
        
        left = self.helper(lists,start,mid)
        right = self.helper(lists,mid+1,end)
        
        return self.merge_two_sorted_lists(left,right)
    
    def merge_two_sorted_lists(self,list1,list2):
        dummy = tail = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next 
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
        

