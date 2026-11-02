class MinStack:

    def __init__(self):
        self.size = 0
        self.arr = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.size += 1
        self.arr.append(val)
        current_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(current_min)

    def pop(self) -> None:
        if self.size == 0:
            return
        self.min_stack.pop()
        self.size -= 1
        return self.arr.pop()
        
    def top(self) -> int:
        if self.size <= 0:
            return
        return self.arr[self.size - 1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
