class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if self.minStack:
            if self.minStack[-1] > x:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.minStack.pop()

    # @return an integer
    def top(self):
        return -1 if len(self.stack) == 0 else self.stack[-1]

    # @return an integer

    def getMin(self):
        return -1 if len(self.minStack) == 0 else self.minStack[-1]


# Test cases
minStack = MinStack()
minStack.push(6)
minStack.push(3)
minStack.push(2)
minStack.push(5)
minStack.push(1)
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.getMin()
