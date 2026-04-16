class MyQueue:

    def __init__(self):
        self.q = []

    def queue(self, x: int) -> None:
        self.q.append(x)

    def dequeue(self) -> int:
        if len(self.q) == 0:
            return None
        x = self.q[0]
        self.q = self.q[1:]
        return x
        
    def empty(self) -> bool:
        return len(self.q) == 0

    def size(self) -> int:
        return len(self.q)


class MyStack:

    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def push(self, x: int) -> None:
        self.q1.queue(x)

    def pop(self) -> int:
        for i in range(self.q1.size()-1):
            x = self.q1.dequeue()
            self.q2.queue(x)
        x = self.q1.dequeue()
        while not self.q2.empty():
            y = self.q2.dequeue()
            self.q1.queue(y)
        return x

    def top(self) -> int:
        for i in range(self.q1.size()):
            x = self.q1.dequeue()
            self.q2.queue(x)
        while not self.q2.empty():
            y = self.q2.dequeue()
            self.q1.queue(y)
        return x
        
    def empty(self) -> bool:
        return self.q1.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()