class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t in operators:
                o2 = stack.pop()
                o1 = stack.pop()

                match t:
                    case '+':
                        stack.append(o1 + o2)
                    case '-':
                        stack.append(o1 - o2)
                    case '*':
                        stack.append(o1 * o2)
                    case '/':
                        stack.append(int(o1 / o2))
            else:
                stack.append(int(t))
            # print(stack)

        return stack[0]


