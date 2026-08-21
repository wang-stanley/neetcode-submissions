class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                match ch:
                    case ')':
                        if stack.pop() != '(':
                            return False
                    case ']':
                        if stack.pop() != '[':
                            return False
                    case '}':
                        if stack.pop() != '{':
                            return False
        
        if len(stack) != 0:
            return False

        return True