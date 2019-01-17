
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        # use queue
        import queue 
        self.size = size
        self.queue = queue.Queue()
        self.sum = 0.0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.sum += val 
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum * 1.0/self.queue.qsize()
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)