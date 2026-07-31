class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = list()
        closing = list(")}]")
        opening = list("({[")
        index = 0
        for char in s:
            if char in opening:
                # index = opening.index(char)
                stack.append(char)     
            elif stack:
                if opening.index(stack[-1]) == closing.index(char):
                # if index == closing.index(char):
                    stack.pop()
                # index = closing.index(char)
                else:
                    return False
            else:
                return False
        if not stack:
            return True
        return False
        # return True