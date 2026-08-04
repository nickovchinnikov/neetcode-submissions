class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for c in s:
            if c in closed:
                if not stack or stack.pop() != closed[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
