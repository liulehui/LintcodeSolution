## LinkedList
#### 2. Add Two Numbers
Solutions:  
use a carry flag to store the carry digit   
Time:  O(n) 

#### 141&142. Linked List Cycle I&II
Solutions:    
1. hashtable  
2. fast and slow two pointers  
Time: O(n)  
if you want to find the index into the loop, hashtable is acceptable.  
While we can also use, **Approach 2**: Floyd's Tortoise and Hare.  
First, determine if there is a loop.   
Next, use a third pointer in the start, another fourth one in the intersection pointer. Both increase by 1 until they meet. 
Note: only with to judge if exists, use only **fast and fast.next**   
Time: O(n)

#### 160. Intersection of Two Linked Lists 
Solutions:  
two pointers  
p1 at headA, p2 at headB  
if p1 reach the end, p1 = headB  
if p2 reach the end, p1 = headA
if they meet, than return   
if they do not meet, than return None

#### 203. Remove Linked List Elements
SOlutions:  
First, add one dummy in front   
Then we will just follow the process.  

#### 234. Palindrome Linked List
Solutions:  
first, find the middle point use two pointers  
second, reverse the second half the the list  
next, compare two halfs  
**Note:**  
to reverse a linkedlist:
  
```
new_head = None         
while slow:
    nxt = slow.next
    slow.next = new_head
    new_head = slow
    slow = nxt
```
Time: O(n)

#### 92. Reverse Linked List II
Solutions:  
Core:  use the above reverse method  
First, find the node that began to reverse and name it tail.  
Its prev name it connect.  
Then reverse between m,n   
e.g. 1->2->3->4->5 m = 2, n = 4  
First:  
con = prev = 1 tail = cur = 2  
Then 4->3->2->1 **prev** now is 4
con.next = prev 1->4->3->2   
finally 2.next = cur 2->5 

#### 430. Flatten a Multilevel Doubly Linked List
Solutions:  
Use a p pointer to stop at where we have a child.      
If we have a child, we find its  tail and append it to p.next.  
Then p.next = p.child.  

#### 138. Copy List with Random Pointer
Solutions:  
Use a hashmap to store the mapping between old node and new node.  


  
