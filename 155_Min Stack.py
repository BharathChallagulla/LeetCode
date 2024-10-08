class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stk = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stk.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stk:
            return self.min_stk[-1] 

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()