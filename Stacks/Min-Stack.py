class MinStack(object):
    def __init__(self):
        self.stack= []
        self.min_vals = []
        
    def push(self, ele: int) -> None:
        if len(self.min_vals) == 0 or ele <= self.min_vals[-1]:
            self.min_vals.append(ele)
        self.stack.append(ele)
        
    def pop(self) -> None:
        if len(self.stack) == 0 or len(self.min_vals) == 0:
            return "Stack is empty"
        if self.stack[-1] == self.min_vals[-1]:
            self.min_vals.pop()
            
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) ==0:
            return "Stack is empty" 
        return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.min_vals) == 0:
            return "No min vals" 
        return self.min_vals[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()