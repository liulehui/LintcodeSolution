## Two Pointers
#### 15. 3Sum
Solutions:
First sort the given nums, then iterate every num in nums as the smallest number, then for each i < j < k, use two pointers to seek nums[j] + nums[k] == -nums[i]