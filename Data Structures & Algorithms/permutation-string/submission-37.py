class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # total = sum(map(ord, s1))
        i = 0
        while i < len(s2)-len(s1)+1:
            if Counter(s2[i:i+len(s1)]) == Counter(s1): 
                if sorted(s1) == sorted(s2[i:i+len(s1)]):
                    return True
            i += 1
        return False
            