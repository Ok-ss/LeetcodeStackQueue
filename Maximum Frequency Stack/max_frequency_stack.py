from collections import deque


class FreqStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        max_fr = 0
        res = None
        for el in self.stack:
            if self.stack.count(el) >= max_fr:
                max_fr = self.stack.count(el)
                res = el
        self.stack.reverse()
        self.stack.remove(res)
        self.stack.reverse()
        return res