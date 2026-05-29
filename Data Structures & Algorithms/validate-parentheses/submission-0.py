from collections import deque
class Solution:
    def isValid(self, st: str) -> bool:
        if len(st) < 2:
            return False
        stack = deque()
        for s in st:
            if s in '([{':
                stack.append(s)
            else:
                if len(stack) > 0:
                    if s is ')':
                        if stack.pop() != '(':
                            return False
                    if s is ']':
                        if stack.pop() != '[':
                            return False
                    if s is '}':
                        if stack.pop() != '{':
                            return False
                else:
                    return False
        return True if len(stack) == 0 else False