# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # set up a dummy node
        self.head = ListNode(0)
        self.tail = self.head
        
        # if l1.val == l2.val and l1.val == 0:
        #     return ListNode(0)
        carry_from_last = 0
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            # print(l1.val)
            if l1:
                l1_val = l1.val
                l1 = l1.next
                print(l1_val)
            if l2:
                l2_val = l2.val
                l2 = l2.next
                print(l2_val)
            
            value = (l1_val+l2_val+carry_from_last) % 10
            carry_from_last = (l1_val+l2_val+carry_from_last) // 10
            print(value,carry_from_last)
            
            self.tail.next  = ListNode(value)
            self.tail = self.tail.next
            
        if carry_from_last:
            self.tail.next = ListNode(carry_from_last)
            self.tail = self.tail.next
        return self.head.next 

if __name__ == '__main__':
    solution = Solution()
    lst1 = ListNode(0)
    lst1.next = ListNode(8)
    lst2 = ListNode(0)
    lst2.next = ListNode(9)

    head = solution.addTwoNumbers(lst1,lst2)
    print('======result======')
    while head:
        print(head.val)
        head = head.next
            
        
        