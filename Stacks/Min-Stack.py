"""
Examples 
   Given stack = [3,1,2]
   push(4) gives [3,1,2,4]
   pop() returns 4
   getMin() returns 1
  
Steps
    For Push:
     1. Check if new element lesser than than current minimum element and store if true.
     2. Add new element to main stack.
     3. Time complexity is O(1), Space complexity is O(1)

    For Pop:
     1. Check for empty stack.
     2. Check if current minimum element matches the element about to be popped.
     3. Pop from the main stack.
     4. Time complexity is O(1), Space complexity is O(1).

    For getMin:
    1. We simply return the element at the top of the stack which stores minimum elements.
    2. Time complexity is O(1), Space complexity is O(1).

"""

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_vals_stack = [float("inf")]
        
    def push(self, ele: int) -> None:
        if ele <= self.min_vals_stack[-1]:
            self.min_vals_stack.append(ele)
        self.stack.append(ele)
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return "Stack is empty"
        if self.stack[-1] == self.min_vals_stack[-1]:
            self.min_vals_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) ==0:
            return "Stack is empty" 
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_vals_stack[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()