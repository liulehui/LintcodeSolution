## Hashtable & String
### Hash
#### 242. Valid Anagram
Solution: 

* sort   
Time: O(nlogn)  
* hashtable   
  Space： O(1) for there are only 26 letter  
  Time: O(n)   
  
#### 49. Group Anagrams
Solution:  
  
 Use hashtable:  
 For str in strs first sort it use klogk  
 And then see if the sorted one in the hashtable  
 Use a list to store all the elements has the same sorted value
 
 Time: O(nklogk)
 
#### 380. Insert Delete GetRandom O(1)
Solution:  
 Hashtable + list  
 Use hashtable to store value and its index  
 Remove can be done by swap with the last element in the list and then pop the last one  
 Time: O(1)  
 Space: O(n)
 
### String
#### 791. Custom Sort String
Solution:  
Use a hashtable to store all the element in the target string. and then sort it accordingly.   
Time : O(n)  Space: O(n)
Follow up:   
What if you cannot use extra space? 

#### 567. Permutation in String
Solutions:  
brute force: find all the permutation of s1 to see if one of them is in s2  
Time: O(l1!)  
Optimization:  
Sliding window + hashtable
Time: O(26 * (l2-l1))

#### 438. Find All Anagrams in a String
Solution:  
Similar to the previous one.  
Hashtable + two pointers  
Time:O(n) Space: O(1)

#### 76. Minimum Window Substring
Solution:
Hashtable for char occurrences  
Two Pointers:  
If we want to include more char into the window, move the right pointer right.  
If we want ot exclude more char from window, move the left pointer right.  
During the process, save the minimum window.  
Time: O(n) Space:O(1)

#### 539. Minimum Time Difference
Solution:  
First, convert the hour:minute time into minute only format.  
Then, sort it.   
Time: O(nlogn)

#### 713. Subarray Product Less Than K
Solutions:  
sliding window  
First, expand the right pointer, for each right pointer meet the requirement, we have right - left + 1 subarrays.  