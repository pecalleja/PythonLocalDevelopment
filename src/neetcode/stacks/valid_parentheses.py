class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for e in s:
            if e in brackets.values():
                stack.append(e)
            elif stack and stack[-1] == brackets[e]:
                stack.pop(-1)
            else:
                return False
        return True if not stack else False
