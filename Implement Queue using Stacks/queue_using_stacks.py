from collections import deque


class Stack:
    def __init__(self):
        self.__deq = deque()
    
    def __repr__(self) -> str:
        return f'{self.__deq}'

    def push(self, x: int) -> None:
        self.__deq.append(x)

    def pop(self) -> int:
        return self.__deq.pop()

    def top(self) -> int:
        res = None
        for el in self.__deq:
            res = el
        return res

    def empty(self) -> bool:
        return not self.size()
    
    def size(self) -> int:
        i = 0
        for _ in self.__deq:
            i+=1
        return i

class MyQueue:

    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        if self.stack.size() > 1:
            reserve = Stack()
            reserve.push(self.stack.pop())
            if self.stack.size() == 1:
                res = self.stack.pop()
            else:
                res = self.pop()
            self.stack.push(reserve.pop())
            return res
        return self.stack.pop()

    def peek(self) -> int:
        if self.stack.size() > 1:
            reserve = Stack()
            reserve.push(self.stack.pop())
            if self.stack.size() == 1:
                res = self.stack.pop()
                self.stack.push(res)
            else:
                res = self.peek()
            self.stack.push(reserve.pop())
            return res
        return self.stack.top()


    def empty(self) -> bool:
        return self.stack.empty()

queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
# print(queue.peek())
# print(queue.stack._Stack__deq)
queue.stack._Stack__deq.clear()
print(queue.stack.empty())
print(queue.empty())
queue.push(1)
print(queue.peek())
print(queue.pop())