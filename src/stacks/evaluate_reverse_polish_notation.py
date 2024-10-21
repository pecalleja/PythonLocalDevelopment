from typing import List


class Solution:
    operation = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b,
    }

    def is_integer(self, n):
        try:
            int(n)
        except ValueError:
            return False
        return True

    def evalRPN(self, tokens: List[str]) -> int:
        current = 0
        while len(tokens) > 1:
            while tokens[current] not in "+-*/":
                current += 1
            operand = tokens[current]
            a = int(tokens[current - 2])
            b = int(tokens[current - 1])
            tokens[current] = self.operation[operand](a, b)
            tokens.pop(current - 2)
            tokens.pop(current - 2)
            current -= 1
        return int(tokens[0])
