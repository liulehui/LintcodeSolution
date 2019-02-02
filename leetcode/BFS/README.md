## BFS
#### 102. Binary Tree Level Order Traversal

solutions:  
1. recursive  
2. iterative  
	use queue  
	Time: O(n)  
	Space: O(n) 


#### 101. Symmetric Tree
Solutions:

1. iterative    
	use queue  
	First append two root in the queue.    
	Everytime pop two node from queue and check whether they are equal or not.    
	Everytime append, append node1.left and node2.right first and then node1.right and node2.left
2. recursive  
	if a tree is sysmmetric:  
Then the two subtree are sysmmetric  

	two trees are sysmmetric:
root.val are the same  
tree1's left substree and tree2's right subtree are sysmmetric  

#### 207&210 Course Schedule I&II  
Solutions:  
Use BFS to do Topological Sorting  
1. initialize and calculate indegree  
2. use queue to store all the elements indegree == 0  
3. pop element in the queue and find its neighbors and all the neighbors' indegree -= 1  
4. if indegree == 0 add it to queue

#### 127. Word Ladder  
Solutions:  
Implicit Graph  

use BFS plus need to record the level  

#### 