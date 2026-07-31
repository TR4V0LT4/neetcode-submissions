class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordcount = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            wordcount[key].append(word)
                
        return list(wordcount.values())


        