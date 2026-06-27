class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.current_min = 0
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        

    def top(self) -> int:
         return self.stack[-1]
        

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        # pop all values in the stack to find min
        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        # restore the stack
        while len(tmp):
            self.stack.append(tmp.pop())

        return mini

        

        
