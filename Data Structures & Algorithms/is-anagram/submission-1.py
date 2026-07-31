class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char in t :
                t = t.replace(char,'',1)
                s = s.replace(char,'',1)
            if t == "" and s == "" :
                return True
        return False
