class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 != 0:
        #     return False
        stack = list()
        closing = list(")}]")
        opening = list("({[")
        index = 0
        for char in s:
            if char in opening:
                stack.append(char)     
            elif stack:
                if opening.index(stack[-1]) == closing.index(char):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        return False
        # return True