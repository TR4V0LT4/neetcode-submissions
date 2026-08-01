class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

        for char in s:
            if char in pairs.values():
                stack.append(char)
            elif not stack or stack[-1] != pairs[char]:
                return False
            else: 
                stack.pop()
        return not stack
