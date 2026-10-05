class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub = list(s1)
        string = list(s2)
        total = sum(ord(c) for c in s1)
        i = 0

        while i < len(s2)-len(s1)+1:
            sumo = 0
            j = i
            for index in range(len(s1)):
                sumo += ord(string[i+index])

            if sumo == total:
                new = s2[i:i+len(s1)]
                print(s2[i:i+len(s1)])
                if sorted(sub) == sorted(new):
                    return True
            i += 1
        return False
            