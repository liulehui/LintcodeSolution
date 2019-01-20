class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.number_to_index = {}
        self.number = []
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.number_to_index:
            return False
        self.number_to_index[val] = len(self.number)
        self.number.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.number_to_index:
            return False
        index = self.number_to_index[val]
        #last = len(self.number) - 1
        self.number_to_index[self.number[-1]] = index
        self.number[-1],self.number[index] = self.number[index],self.number[-1]
        self.number.pop()
        del self.number_to_index[val]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.choice(self.number)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()