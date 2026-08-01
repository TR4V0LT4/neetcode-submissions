class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       operators = set(['+' , '-' , '*', '/'])
       stack = []
       for item in tokens:
        if item in operators:
            right = stack.pop()
            left =  stack.pop()
            if item == '+':
                stack.append(right + left)
            elif item == '-':
                stack.append(left - right)
            elif item == '*':
                stack.append(right * left)
            elif item == '/':
                if right != 0:
                    stack.append(int(left/right))
        else:
            stack.append(int(item))
       return stack[-1]
