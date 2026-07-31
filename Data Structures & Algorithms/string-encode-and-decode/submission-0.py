class Solution:

    def encode(self, strs: List[str]) -> str:
        hash = ""
        for s in strs:
            hash += str(len(s)) + "#" + s
        return hash

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            lenght = int(s[i:j])

            word = s[j+1:j+lenght+1]

            result.append(word)
            i = j + lenght + 1
            
        return result
                 
            


        
