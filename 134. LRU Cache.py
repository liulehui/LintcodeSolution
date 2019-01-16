# coding:utf-8
# Solution 1 : use hash to remember the prev node
class LinkedNode:
    def __init__(self,key=None,value=None,next = None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head 
        self.capacity = capacity
    
    def push_back(self,node):
        self.hash[node.key] = self.tail 
        self.tail.next = node 
        self.tail = node 
    
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next 
        self.hash[self.head.next.key] = self.head
        
    # change "prev->node->next->...->tail"
    # to "prev->next->...->tail->node"
    
    def kick(self,prev):
        node = prev.next 
        if node == self.tail:
            return 
        prev.next = node.next 
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None 
        self.push_back(node)
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.hash:
            return -1 
        self.kick(self.hash[key])
        return self.hash[key].next.value 
    
        
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value 
        else:
            self.push_back(LinkedNode(key,value))
            if len(self.hash) > self.capacity:
                self.pop_front()

# Solution 2: use double linked list and hash 
# This soluiton is very straightforward
class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(-1,-1) # dummy node
        self.tail = Node(-1, -1) # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.hash: return -1 
        node = self.hash[key]
        self.remove_node(node)
        self.move_to_tail(node)
        return node.val 
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if self.get(key) != -1:
            self.hash[key].val = value
            return 
        if len(self.hash) >= self.capacity:
            self.pop_front()
        node = Node(key, value)
        self.move_to_tail(node)
        self.hash[key] = node
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def move_to_tail(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail 
        node.prev.next = node 
        self.tail.prev = node
        
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

