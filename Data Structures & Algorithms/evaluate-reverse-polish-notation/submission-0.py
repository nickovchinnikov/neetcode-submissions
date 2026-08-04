class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}

        stack = []
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(a-b)
                elif t == "*":
                    stack.append(a*b)
                elif t == "/":
                    stack.append(int(a/b))
        return stack[0]


