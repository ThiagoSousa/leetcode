class MyStack:

    def __init__(self):
        self.s = []
    
    def stack(self, x: int) -> None:
        self.s.append(x)

    def unstack(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        if len(self.s) == 0:
            return None
        return self.s[-1]
    
    def empty(self) -> bool:
        return len(self.s) == 0

class MyQueue:

    def __init__(self):
        self.s1 = MyStack()
        self.s2 = MyStack()
        
    def push(self, x: int) -> None:
        self.s1.stack(x)

    def pop(self) -> int:
        while not self.s1.empty():
            self.s2.stack(self.s1.unstack())
        x = self.s2.unstack()
        while not self.s2.empty():
            self.s1.stack(self.s2.unstack())
        return x
        
    def peek(self) -> int:
        while not self.s1.empty():
            self.s2.stack(self.s1.unstack())
        x = self.s2.peek()
        while not self.s2.empty():
            self.s1.stack(self.s2.unstack())
        return x
        
    def empty(self) -> bool:
        return self.s1.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()