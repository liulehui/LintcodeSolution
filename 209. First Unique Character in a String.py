# coding:utf-8
# normal one can be iterated twice
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        count = {}
        # only 256 ascii space
        for i in str:
            if i in count:
                count[i] += 1 
            else:
                count[i] = 1  
        
        for i in str:
            if count[i] == 1:
                return i 


# what if it is a data stream?
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        ds = DataStream()
        for i in range(len(str)):
            ds.add(str[i])
        
        return ds.firstUniqueChar()
        

class ListCharNode:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next 
    
class DataStream:
    def __init__(self,charToPrev ={},dupChars = set()):
        self.charToPrev = charToPrev
        self.dupChars = dupChars
        self.dummy = ListCharNode('.')
        self.tail = self.dummy
    
    def add(self,c):
        if c in self.dupChars:
            return 
        if c not in self.charToPrev:
            node = ListCharNode(c) 
            self.charToPrev[c] = self.tail 
            self.tail.next = node 
            self.tail = node 
            return 
        # deleting the existing node 
        prev = self.charToPrev[c]
        prev.next = prev.next.next 
        if prev.next is None:
            # tail node removed
            self.tail = prev 
        
        else:
            self.charToPrev[prev.next.val] = prev 
        
        self.charToPrev.pop(c)
        self.dupChars.add(c)
    def firstUniqueChar(self):
        return self.dummy.next.val
        
