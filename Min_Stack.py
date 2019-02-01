class MinStack(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = 0

    def push(self, value):
        """
        :type x: int
        :rtype: void
        """
        minimum = self.getMin()
        if(value < minimum or minimum==None):
            minimum = value
        self.stack.append((value,minimum))
        
    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return(None)
        return(self.stack[-1][0])

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return(None)
        return(self.stack[-1][1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
