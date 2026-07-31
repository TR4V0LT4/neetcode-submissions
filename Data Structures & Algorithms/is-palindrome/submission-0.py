class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        # s = s.strip().lower()
        s = "".join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(s) -1
        # print(s)
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True