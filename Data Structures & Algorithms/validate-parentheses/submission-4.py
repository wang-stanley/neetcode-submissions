class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in bracketMapping:
                if len(stack) == 0 or stack.pop() != bracketMapping[ch]:
                    return False
            else:
                stack.append(ch)
        
        if len(stack) != 0:
            return False

        return True