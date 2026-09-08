class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.heap or val < self.heap[-1]:
            self.heap.append(val)
        else:
            self.heap.append(self.heap[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.heap.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.heap[-1]
        
        
