class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        self.visited = {}
        if not head:
            return head
        old_node = head
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node
        
        while old_node != None:
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)
            
            old_node = old_node.next
            new_node = new_node.next
        
        return self.visited[head]
    
    def getCloneNode(self,node):
        if node:
            
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        
        return None
     