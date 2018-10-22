class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mstk = []
        return None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.mstk.append(x)
        #self.insert(-1,x)

    def pop(self):
        """
        :rtype: void
        """
        self.mstk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mstk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.mstk)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
