from collections import deque

class Queue:
    def __init__(self) -> None:
        self.__deq = deque()

    def __repr__(self) -> str:
        return f'{self.__deq}'
        
    def push(self, x:int) -> None:
        self.__deq.append(x)
    
    def pop(self) -> int:
        return self.__deq.popleft()

    def peek(self) -> int:
        for el in self.__deq:
            return el

    def size(self) -> int:
        i = 0
        for _ in self.__deq:
            i+=1
        return i

    def empty(self) -> bool:
        return not self.size()

class MyStack:

    def __init__(self):
        self.q = Queue()

    def __repr__(self) -> str:
        return f'{self.q}'
        
    def push(self, x: int) -> None:
        self.q.push(x)

    def pop(self) -> int:
        i = 1
        while i < self.q.size():
            self.q.push(self.q.pop())
            i+=1
        return self.q.pop()

    def top(self) -> int:
        i = 1
        while i < self.q.size():
            self.q.push(self.q.pop())
            i+=1
        res = self.q.pop()
        self.q.push(res)
        return res

    def empty(self) -> bool:
        return self.q.empty()

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())