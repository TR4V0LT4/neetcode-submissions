class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        total = sum(map(ord, s1))
        i = 0

        while i < len(s2)-len(s1)+1:
            sumo = sum(map(ord, s2[i:i+len(s1)]))
            if sumo == total:
                new = s2[i:i+len(s1)]
                if sorted(s1) == sorted(new):
                    return True
            i += 1
        return False
            