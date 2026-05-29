from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = deque()
        for t in tokens:
            if t not in '+-*/':
                num.append(int(t))
            else:
                b,a = num.pop(), num.pop()
                num.append(int(a + b) if t == '+' else
                int(a - b) if t == '-' else
                int(a * b) if t == '*' else
                int(a / b))
        return num[-1]