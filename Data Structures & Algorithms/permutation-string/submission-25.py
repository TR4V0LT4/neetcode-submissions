class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        total = sum(ord(c) for c in s1)
        i = 0

        while i < len(s2)-len(s1)+1:
            sumo = 0
            if s2[i] in s1: 
                for index in range(len(s1)):
                    sumo += ord(s2[i+index])

                if sumo == total:
                    new = s2[i:i+len(s1)]
                    if sorted(s1) == sorted(new):
                        return True
            i += 1
        return False
            