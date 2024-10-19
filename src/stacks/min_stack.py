class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            last = self.stack[-1]
            self.stack.append((val, min(last[-1], val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
